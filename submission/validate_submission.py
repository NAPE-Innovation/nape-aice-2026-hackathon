"""Participant-side submission checks; no reference answers or scoring."""
import argparse
import csv
import json
import math
from pathlib import Path

HEADERS = {
    "1": ("page_id", "well", "depth_m", "curve", "value", "confidence", "notes"),
    "2": ("question_id", "answer", "evidence", "confidence", "notes"),
}

def validate_structure(folder):
    folder = Path(folder)
    errors = []
    for name in ("README.md", "requirements.txt", "predictions.csv"):
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

def validate_csv(path, track):
    path = Path(path)
    errors = []
    if not path.is_file():
        return {"valid": False, "errors": ["Predictions CSV not found"], "rows": 0}
    try:
        with path.open(encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            columns = reader.fieldnames or []
            missing = [name for name in HEADERS[track] if name not in columns]
            if missing:
                errors.append("Missing columns: " + ", ".join(missing))
            if len(columns) != len(set(columns)):
                errors.append("Duplicate CSV column headers")
            rows = list(reader)
    except (UnicodeDecodeError, csv.Error) as exc:
        return {"valid": False, "errors": [f"Unreadable CSV: {exc}"], "rows": 0}
    keys = ("page_id", "depth_m", "curve") if track == "1" else ("question_id",)
    seen = set()
    for number, row in enumerate(rows, 2):
        if None in row or any(v is None for v in row.values()):
            errors.append(f"Line {number}: incorrect number of columns")
            continue
        key = tuple((row.get(k) or "").strip() for k in keys)
        if not all(key):
            errors.append(f"Line {number}: missing identifier")
        elif key in seen:
            errors.append(f"Line {number}: duplicate identifier")
        seen.add(key)
        if track == "1":
            for field in ("depth_m", "value"):
                try:
                    value = float(row.get(field, ""))
                    if not math.isfinite(value):
                        errors.append(f"Line {number}: non-finite {field}")
                except (ValueError, TypeError):
                    errors.append(f"Line {number}: invalid {field}")
        if (row.get("confidence") or "").strip():
            try:
                confidence = float(row["confidence"])
                if not math.isfinite(confidence) or not 0 <= confidence <= 1:
                    errors.append(f"Line {number}: confidence must be between 0 and 1")
            except ValueError:
                errors.append(f"Line {number}: invalid confidence")
    if not rows:
        errors.append("CSV has no data rows")
    return {"valid": not errors, "errors": errors, "rows": len(rows)}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--track", choices=["1", "2"], required=True)
    parser.add_argument("--submission", type=Path, required=True)
    args = parser.parse_args()
    report = {
        "structure": validate_structure(args.submission),
        "csv": validate_csv(args.submission / "predictions.csv", args.track),
    }
    print(json.dumps(report, indent=2))
    if not all(section["valid"] for section in report.values()):
        raise SystemExit(1)

if __name__ == "__main__":
    main()
