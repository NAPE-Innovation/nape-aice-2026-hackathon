# Submission Guide — NAPE AICE 2026

This guide applies to both challenge tracks. We have kept the submission format deliberately simple for a student hackathon.

## Required files

Each team submits one folder containing:

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

- **Track 1 — Legacy Well Log Digitisation:** `page_id,well,depth_m,curve,value,confidence,notes`
- **Track 2 — Intelligent Well Archive:** `question_id,answer,evidence,confidence,notes`

Use the provided prediction template for your allocated track. Preserve requested identifiers. The organisers will announce the final submission deadline and handover method.

## How the submission is scored

| Component | Weight |
| --- | ---: |
| Presentation judging | 40% |
| Open-test result, based on `predictions.csv` | 40% |
| Organiser-run inference / reproducibility | 20% |

Open-test predictions are scored by the NAPE team against the approved reference answers. After submission, **NAPE technical reviewers independently run your submitted notebook/code**, following your README and requirements. They assess whether the solution runs without errors, produces valid outputs, can be reproduced and how long it takes under an agreed execution environment. Teams do **not** need to execute their notebooks live during the presentation. There is **no automated hidden-test scoring**.

For fairness, organiser-run execution uses consistent hardware/resources and documented timing rules across teams. Reference answers are never supplied in the public submission package.

## Check your submission

From the hackathon repository, run:

```bash
python submission/validate_submission.py --track 1 --submission /path/to/submission
# Or use --track 2 for Archive Intelligence
```

The check confirms required files, notebook structure and basic prediction CSV integrity. It does **not** run the notebook or score prediction quality.

See [Competition Rules](../docs/competition-rules.md) and [Participant Technical Guide](../docs/participant-technical-guide.md).
