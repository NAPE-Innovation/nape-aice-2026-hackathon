#!/usr/bin/env python3
"""Check the format of a NAPE AICE 2026 hackathon submission.

This checks files, columns and identifiers only. It does not score answers
or run your notebook. It applies the same row rules as the organisers'
scoring, so a CSV that passes here will not be rejected for its format.

Run it from the repository root:

    python submission/validate_submission.py --track 1 ../nape-aice-2026-your-team/submission

or import it in a notebook:

    from validate_submission import validate_submission
    report = validate_submission("../nape-aice-2026-your-team/submission", track=1)
"""
from __future__ import annotations

import argparse
import csv
import json
import math
import sys
from pathlib import Path

# Columns every predictions.csv must have, per track.
REQUIRED_COLUMNS = {
    1: ("page_id", "well", "depth_m", "curve", "value", "confidence"),
    2: ("question_id", "answer", "evidence", "confidence"),
}
# Columns that may be added. Any other column is reported as a warning.
OPTIONAL_COLUMNS = {
    1: ("notes",),
    2: ("notes",),
}
REQUIRED_FILES = ("README.md", "requirements.txt", "predictions.csv")

# Where the published targets and questions live, relative to data/track_N.
EXPECTED_ROWS_FILE = {
    1: Path("metadata") / "target_depths_template.csv",
    2: Path("open_test") / "open_test_questions.csv",
}


def find_data_root(track: int, start: Path | None = None) -> Path | None:
    """Find data/track_N from the repository root, a starter-kit folder or this folder."""
    start = Path(start or Path.cwd()).resolve()
    here = Path(__file__).resolve().parent
    for base in (start, start.parent, start.parent.parent, here.parent):
        candidate = base / "data" / f"track_{track}"
        if candidate.is_dir():
            return candidate
    return None


def _key(row: dict, track: int) -> tuple:
    """Identifier used to match a row with its target or question."""
    if track == 1:
        return (
            (row.get("page_id") or "").strip(),
            f"{float(row['depth_m']):.2f}",
            (row.get("curve") or "").strip().upper(),
        )
    return ((row.get("question_id") or "").strip(),)


def _well(value: str) -> str:
    return (value or "").strip().upper().replace("/", "_")


def _read_csv(path: Path) -> tuple[list[str], list[dict]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def load_expected(track: int, data_root: Path | None = None) -> dict | None:
    """Return the published targets (Track 1) or questions (Track 2), keyed by identifier."""
    data_root = Path(data_root) if data_root else find_data_root(track)
    if not data_root:
        return None
    path = data_root / EXPECTED_ROWS_FILE[track]
    if not path.is_file():
        return None
    _, rows = _read_csv(path)
    return {_key(row, track): row for row in rows}


def validate_structure(folder) -> dict:
    """Check the submission folder has the required files and a readable notebook."""
    folder = Path(folder)
    errors = []
    for name in REQUIRED_FILES:
        path = folder / name
        if not path.is_file() or not path.read_text(encoding="utf-8").strip():
            errors.append("Missing or empty required file: " + name)
    notebooks = sorted(folder.glob("*.ipynb"))
    if not notebooks:
        errors.append("At least one Jupyter notebook (.ipynb) is required")
    for notebook in notebooks:
        try:
            data = json.loads(notebook.read_text(encoding="utf-8"))
            if not isinstance(data.get("nbformat"), int) or not isinstance(data.get("cells"), list):
                errors.append("Invalid notebook structure: " + notebook.name)
        except (json.JSONDecodeError, UnicodeDecodeError):
            errors.append("Unreadable notebook: " + notebook.name)
    return {"valid": not errors, "errors": errors, "notebooks": len(notebooks)}


def validate_csv(path, track: int, expected: dict | None = None) -> dict:
    """Check predictions.csv columns, values and identifiers.

    If `expected` (from load_expected) is given, also check every row matches a
    published target or question. Missing targets are warnings because they
    simply score zero; unknown targets are errors because scoring rejects them.
    """
    track = int(track)
    path = Path(path)
    errors, warnings = [], []
    if not path.is_file():
        return {"valid": False, "errors": ["Predictions CSV not found"], "warnings": [], "rows": 0}
    try:
        columns, rows = _read_csv(path)
    except (UnicodeDecodeError, csv.Error) as exc:
        return {"valid": False, "errors": [f"Unreadable CSV: {exc}"], "warnings": [], "rows": 0}

    missing = [name for name in REQUIRED_COLUMNS[track] if name not in columns]
    if missing:
        errors.append("Missing columns: " + ", ".join(missing))
    if len(columns) != len(set(columns)):
        errors.append("Duplicate CSV column headers")
    extra = [name for name in columns if name not in REQUIRED_COLUMNS[track] + OPTIONAL_COLUMNS[track]]
    if extra:
        warnings.append("Unexpected columns (ignored in scoring): " + ", ".join(extra))
    if missing:
        return {"valid": False, "errors": errors, "warnings": warnings, "rows": len(rows)}

    seen = set()
    unknown = 0
    for number, row in enumerate(rows, 2):
        if None in row or any(v is None for v in row.values()):
            errors.append(f"Line {number}: incorrect number of columns")
            continue
        try:
            key = _key(row, track)
        except ValueError:
            errors.append(f"Line {number}: invalid depth_m")
            continue
        if not all(key):
            errors.append(f"Line {number}: missing identifier")
            continue
        if key in seen:
            errors.append(f"Line {number}: duplicate identifier {key}")
        seen.add(key)

        if track == 1:
            if not (row.get("well") or "").strip():
                errors.append(f"Line {number}: missing well")
            depth = float(row["depth_m"])
            if not math.isfinite(depth):
                errors.append(f"Line {number}: non-finite depth_m")
            value = (row.get("value") or "").strip()
            if value:  # blank means no reading was extracted; it scores zero
                try:
                    if not math.isfinite(float(value)):
                        errors.append(f"Line {number}: non-finite value")
                except ValueError:
                    errors.append(f"Line {number}: invalid value")

        confidence = (row.get("confidence") or "").strip()
        if confidence:
            try:
                number_value = float(confidence)
                if not math.isfinite(number_value) or not 0 <= number_value <= 1:
                    errors.append(f"Line {number}: confidence must be between 0 and 1")
            except ValueError:
                errors.append(f"Line {number}: invalid confidence")

        if expected is not None:
            target = expected.get(key)
            if target is None:
                unknown += 1
                if unknown <= 5:
                    errors.append(f"Line {number}: {key} is not a published target or question")
            elif track == 1 and _well(row.get("well")) != _well(target.get("well")):
                errors.append(f"Line {number}: wrong well for {key}")

    if unknown > 5:
        errors.append(f"{unknown} rows in total are not published targets or questions")
    if not rows:
        errors.append("CSV has no data rows")
    if expected is not None:
        absent = len(set(expected) - seen)
        if absent:
            warnings.append(f"{absent} of {len(expected)} targets or questions have no row; they will score zero")
    return {"valid": not errors, "errors": errors, "warnings": warnings, "rows": len(rows)}


def validate_submission(folder, track: int, data_root=None) -> dict:
    """Check a whole submission folder: required files plus predictions.csv."""
    track = int(track)
    folder = Path(folder)
    expected = load_expected(track, data_root)
    report = {
        "structure": validate_structure(folder),
        "csv": validate_csv(folder / "predictions.csv", track, expected),
    }
    if expected is None:
        report["csv"]["warnings"].append(
            "Published targets/questions not found, so identifiers were not checked against them"
        )
    report["valid"] = report["structure"]["valid"] and report["csv"]["valid"]
    return report


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Check the format of a hackathon submission folder.")
    parser.add_argument("submission_dir", help="Path to your team's submission/ folder")
    parser.add_argument("--track", type=int, choices=(1, 2), required=True)
    parser.add_argument("--data-root", help="Path to data/track_N if it is not found automatically")
    args = parser.parse_args(argv)
    report = validate_submission(args.submission_dir, args.track, args.data_root)
    print(json.dumps(report, indent=2))
    print("PASS: format valid" if report["valid"] else "FAIL: fix the errors above")
    return 0 if report["valid"] else 1


if __name__ == "__main__":
    sys.exit(main())
