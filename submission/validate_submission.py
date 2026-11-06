"""Participant-side submission checks; no reference answers or scoring."""
import argparse
import csv
import json
import math
from pathlib import Path

HEADERS = {
    "1": ("page_id", "well", "depth_m", "curve", "value", "confidence"),
    "2": ("question_id", "answer", "evidence", "confidence"),
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
    from decimal import Decimal, InvalidOperation, ROUND_HALF_EVEN
    errors=[]
    try:
        with Path(path).open(newline='',encoding='utf-8-sig') as handle:
            reader=csv.DictReader(handle)
            fields=reader.fieldnames or []
            if len(fields)!=len(set(fields)) or not set(HEADERS[track]).issubset(fields):
                raise ValueError('Missing or duplicate CSV columns')
            rows=list(reader)
        if not rows:raise ValueError('Predictions CSV is empty')
        seen=set()
        for line,row in enumerate(rows,2):
            if None in row or any(v is None for v in row.values()):
                raise ValueError(f'Row {line}: malformed CSV')
            if track=='1':
                depth=Decimal(row['depth_m'].strip())
                if not depth.is_finite():raise ValueError('Depth must be finite')
                key=(row['page_id'].strip(),str(depth.quantize(Decimal('0.01'),rounding=ROUND_HALF_EVEN)),row['curve'].strip().upper())
                if not row['well'].strip() or key[2] not in {'GR','RT','RHOB','NPHI'}:
                    raise ValueError(f'Row {line}: invalid well or curve')
            else:key=(row['question_id'].strip(),)
            if not all(key) or key in seen:raise ValueError(f'Row {line}: missing or duplicate normalized identifier')
            seen.add(key)
            for field in (['confidence','value'] if track=='1' else ['confidence']):
                text=row[field].strip()
                if not text:continue  # Missing readings and unset confidence are allowed.
                number=float(text)
                if not math.isfinite(number):raise ValueError(f'Row {line}: non-finite {field}')
                if field=='confidence' and not 0<=number<=1:raise ValueError(f'Row {line}: confidence outside [0,1]')
                if field=='value' and key[2]=='RT' and number<=0:raise ValueError(f'Row {line}: RT must be positive')
        return {'valid':True,'errors':[],'rows':len(rows)}
    except (OSError,ValueError,InvalidOperation,csv.Error) as exc:
        return {'valid':False,'errors':[str(exc)],'rows':0}

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
