# Team Submission Template

Copy this template into a folder named after your **registered team name**, using lowercase letters and hyphens instead of spaces (for example, `Team X` → `team-x/` or `Team Alpha` → `team-alpha/`). Replace the example implementation. The folder name is distinct from the organiser-assigned team ID.

```text
team-x/
├── README.md
├── requirements.txt
├── run_inference.py
├── src/                 # optional
├── models/              # if applicable
├── indexes/             # if applicable
└── outputs/
    └── predictions.csv
```

The final handover method is still under organiser review.

## Required
- `run_inference.py`: accepts `--input` and `--output`, writes predictions CSV; implement your actual inference logic.
- `requirements.txt`: pin required Python packages.
- `models/` and `indexes/`: include frozen artefacts if your solution needs them.
- `outputs/predictions.csv`: completed challenge-specific output.
- `README.md`: explain how organisers can run the solution without retraining.

See [Submission Guide](../SUBMISSION_GUIDE.md). The included script is **an interface stub, not a working model or baseline**. Do not submit it unchanged.
