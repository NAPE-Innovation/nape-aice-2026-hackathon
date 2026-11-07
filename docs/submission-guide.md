# Submission Guide — NAPE AICE 2026

This guide applies to both challenge tracks. We have kept the submission format deliberately simple for a student hackathon.

## Required files

Each team must create a **`submission/` directory at the root of their assigned team GitHub repository**. Do not place final deliverables directly in the repository root. The required layout is:

```text
submission/
├── solution.ipynb       # one or more notebooks; filename is flexible
├── predictions.csv      # predictions using the supplied track-specific template
├── requirements.txt     # Python dependencies
└── README.md            # step-by-step instructions for organisers
```

Additional saved model weights, configuration or retrieval indexes may be included **if needed** to reproduce your solution. Teams are not required to build an API, Docker image, CI/CD pipeline or separate `run_inference.py` script.

The README should explain how to prepare the environment, where the input data and any model artefacts belong, which notebook cells to run and in what order, how to generate `predictions.csv`, external services required (if any), and relevant assumptions or limitations. Avoid undocumented interactive steps and never include API keys.

## Track-specific prediction CSVs

- **Track 1 — Legacy Well Log Digitisation:** `page_id,well,depth_m,curve,value,confidence`
- **Track 2 — Intelligent Well Archive:** `question_id,answer,evidence,confidence`

Use the provided prediction template for your allocated track. Preserve requested identifiers. The required prediction path is **`submission/predictions.csv`**. Keep all final deliverables inside `submission/`; supporting artefacts can be stored there in subfolders. Teams may use the repository root for drafts or experiments, but only the final `submission/` directory (and explicitly documented approved dependencies) will be reviewed. The submission deadline is **8 November 2026 at 18:00 WAT (UTC+1)**. Your assigned private team repository's `main` branch is the official submission; no separate email or Drive upload is required unless the organisers announce a contingency. At the deadline, NAPE will record the team repository's commit SHA so the scored CSV and independently executed notebook come from the same version.

## Approved event settings

- **Deadline:** 8 November 2026 at 18:00 WAT (UTC+1).
- **Notebook execution:** 30 minutes on the same organiser hardware for all teams. Organisers prepare approved declared dependencies first, record setup difficulties, then time notebook execution through creation of `predictions.csv`.
- **Tools:** internet, open-source tools and pretrained models are allowed. Paid APIs require equal organiser-approved access. Supplied data must not be uploaded to external services without express approval.
- **Track 2 questions:** answer all 32 questions in [open_test_questions.csv](../data/track_2/open_test/open_test_questions.csv). Use [the supplied answer template](../submission/template/outputs/track2_predictions_template.csv), retaining `T2-001`–`T2-032`. Reference answers remain private.

## How the submission is scored

| Component | Weight |
| --- | ---: |
| Presentation judging | 40% |
| Open-test result, based on `predictions.csv` | 40% |
| Organiser-run inference / reproducibility | 20% |

Open-test predictions are scored by the NAPE team against the approved reference answers. Track 1 uses the numeric curve scorer. For Track 2, judges review all 32 answers: 1 point for a complete correct answer with supporting evidence, 0.5 for a partly correct supported answer, and 0 for an incorrect or unsupported answer. Equivalent correct wording and units are accepted. A clear, correct abstention earns 1 on an unanswerable question; do not invent a citation. The reviewed total divided by 32 and multiplied by 40 is the Track 2 prediction component. Automatic text matching is a preliminary check only. Identify source files and pages/sections in `evidence` so judges can verify claims. After submission, **NAPE technical reviewers independently run your submitted notebook/code**, following your README and requirements. They assess whether the solution runs without errors, produces valid outputs, can be reproduced and how long it takes under an agreed execution environment. Teams do **not** need to execute their notebooks live during the presentation. There is **no automated hidden-test scoring**.

For fairness, organiser-run execution uses consistent hardware/resources and documented timing rules across teams. Reference answers are never supplied in the public submission package.

## Check your submission

For step-by-step cloning, team repository setup and a complete validator example, see the [GitHub Setup and Team Submission Guide](github-setup-and-submission.md).

Open the starter notebook for your assigned track and run its final **Validate Your Submission** cells. Set `SUBMISSION_DIR` to the `submission/` folder in your private team repository. The check reports missing files, malformed notebooks, incorrect CSV headers, duplicate identifiers and invalid values. It does **not** run your solution or score predictions. The [GitHub Setup Guide](github-setup-and-submission.md) contains a worked example.

See [Competition Rules](competition-rules.md) and [Participant Technical Guide](participant-technical-guide.md).
