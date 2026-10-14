"""Participant-side checks. No hidden answers or scoring logic."""
import argparse
import csv
import json
from pathlib import Path

HEADERS = {
    "1": ("page_id", "well", "depth_m", "curve", "value", "confidence", "notes"),
    "2": ("question_id", "answer", "evidence", "confidence", "notes"),
}

def validate_csv(path, track):
    path = Path(path)
    errors = []
    if not path.is_file():
        return {"valid": False, "errors": ["Predictions CSV not found"], "rows": 0}
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        columns = reader.fieldnames or []
        missing = [name for name in HEADERS[track] if name not in columns]
        if missing:
            errors.append("Missing columns: " + ", ".join(missing))
        rows = list(reader)
    keys = ("page_id", "depth_m", "curve") if track == "1" else ("question_id",)
    seen = set()
    for number, row in enumerate(rows, 2):
        key = tuple((row.get(k) or "").strip() for k in keys)
        if not all(key):
            errors.append(f"Line {number}: missing identifier")
        elif key in seen:
            errors.append(f"Line {number}: duplicate identifier")
        seen.add(key)
        if track == "1":
            for field in ("depth_m", "value"):
                try:
                    float(row.get(field, ""))
                except (ValueError, TypeError):
                    errors.append(f"Line {number}: invalid {field}")
        elif not (row.get("answer") or "").strip():
            errors.append(f"Line {number}: empty answer")
        if (row.get("confidence") or "").strip():
            try:
                confidence = float(row["confidence"])
                if not 0 <= confidence <= 1:
                    errors.append(f"Line {number}: confidence must be between 0 and 1")
            except ValueError:
                errors.append(f"Line {number}: invalid confidence")
    if not rows:
        errors.append("CSV has no data rows")
    return {"valid": not errors, "errors": errors, "rows": len(rows)}

def validate_structure(folder):
    folder = Path(folder)
    errors = []
    for name in ("README.md", "requirements.txt", "run_inference.py", "outputs/predictions.csv"):
        if not (folder / name).is_file():
            errors.append("Missing required file: " + name)
    if (folder / "run_inference.py").is_file():
        script = (folder / "run_inference.py").read_text(encoding="utf-8")
        if "NotImplementedError" in script:
            errors.append("Inference entry point appears to be the unchanged template stub")
    return {"valid": not errors, "errors": errors}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--track", choices=["1", "2"], required=True)
    parser.add_argument("--submission", type=Path, required=True)
    args = parser.parse_args()
    report = {"structure": validate_structure(args.submission),
              "csv": validate_csv(args.submission / "outputs/predictions.csv", args.track)}
    print(json.dumps(report, indent=2))
    if not all(section["valid"] for section in report.values()):
        raise SystemExit(1)

if __name__ == "__main__":
    main()
