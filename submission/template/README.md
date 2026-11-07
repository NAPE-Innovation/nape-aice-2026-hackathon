# Student Submission Template

Copy the starter files into a **`submission/` folder at the root of your assigned team GitHub repository**. Do not submit final files at the repository root. For example:

```text
nape-aice-2026-your-team/
└── submission/
    ├── solution.ipynb        # rename if you prefer
    ├── predictions.csv       # your completed predictions
    ├── requirements.txt      # dependencies
    └── README.md             # setup and running instructions
```

Use the track-specific prediction CSV template available under `outputs/` in this hackathon repository as a starting point. Each template already lists every target (Track 1) or question (Track 2). Copy/rename it to `predictions.csv` in your submission folder before handover. The included `solution.ipynb` is an empty placeholder: replace its contents with your work.

In your submission's README, explain how NAPE reviewers can install requirements, access the input dataset, run the notebook from the beginning and regenerate the predictions. Include any necessary model/index files or instructions for accessing approved services. Do not include secrets.

A separate `run_inference.py`, API, Docker image or CI/CD configuration is **not required**. NAPE will run your code after submission and assess reproducibility as part of the 20% inference score.

**Fixed automated scoring path:** `submission/predictions.csv`. The organisers will record the final commit SHA at the submission deadline. See [Submission Guide](../../docs/submission-guide.md).
