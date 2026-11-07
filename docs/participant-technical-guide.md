# Participant Technical Guide

**NAPE AICE 2026 Hackathon | 7–8 November 2026 | Both tracks**

The [Challenge Brief](../CHALLENGE_BRIEF.md) defines the tasks and prediction formats. The [Submission Guide](submission-guide.md) explains how to submit. Starter notebooks are optional teaching aids, not finished solutions.

## 1. Set up your environment

Use the approved track-specific data from this repository or the organiser-provided team laptop. See [Data Access](data-access.md) for paths. Inspect your track's input manifest and CSV template. Never upload restricted data to unauthorised external services, and never include credentials or supplied raw datasets in your code submission.

You may use Python packages, pretrained models and approved APIs in accordance with the [Competition Rules](competition-rules.md). List dependencies in `requirements.txt` and disclose relevant third-party services.

## 2. Build your solution

You can implement your approach in one or more **Jupyter notebooks**, including preprocessing, extraction, model training, retrieval, generation and prediction as appropriate. You do not have to package your code as a production application or write a separate inference command.

**Track 1 — Legacy Well Log Digitisation:** use the approved log images/PDFs and metadata to produce `page_id,well,depth_m,curve,value,confidence` (optional `notes`), at the published target depths or as full extracted logs. Only the target depths are scored, using your reading at the nearest submitted depth within 0.10 m. [Track 1 starter notebook](../starter-kits/track-1/log_digitisation_starter.ipynb).

**Track 2 — Intelligent Well Archive:** use the approved archive and open questions to produce `question_id,answer,evidence,confidence`. Evidence should identify supporting archive documents. [Track 2 starter notebook](../starter-kits/track-2/archive_intelligence_starter.ipynb).

The starter notebooks demonstrate techniques or input inspection but are not complete competition submissions.

## 3. Make your work reproducible

Before submitting, restart the notebook kernel and, where possible, run the notebook cells in order. Include any required model files, fitted preprocessing, saved indexes or configuration when applicable. Document the exact steps to get from the approved input data to `predictions.csv`; clearly state whether training or index preparation must be performed as part of those steps.

Provide a `README.md` with setup and run instructions, input paths, package versions, expected output location, runtime assumptions, external APIs or licences, methodology and limitations. Include `requirements.txt`. Never include credentials. If your solution depends on network services, disclose that so organisers can verify whether they are permitted and available.

## 4. Prepare the submission

Include:
1. Your solution notebook(s) (`.ipynb`).
2. Completed `predictions.csv` using the provided template.
3. `requirements.txt`.
4. `README.md` describing how the NAPE technical team can reproduce your output.

Additional model or index files are optional if relevant. No Docker image, API, CI/CD project or `run_inference.py` is required.

Validate the submission using the final **Validate Your Submission** cells in the [Track 1](../starter-kits/track-1/log_digitisation_starter.ipynb) or [Track 2](../starter-kits/track-2/archive_intelligence_starter.ipynb) starter notebook. Set `SUBMISSION_DIR` to your team repository's `submission/` folder. This checks structure and CSV integrity, not solution execution or accuracy.

## 5. Judging and technical review

**Presentation judging (40%):** teams present and explain their solution; live notebook execution is not mandatory.

**Open-test score (40%):** organisers score the submitted prediction CSV against the approved reference.

**Inference / reproducibility (20%):** after submission, NAPE reviewers execute the team's submitted notebook/code independently using its requirements and instructions, then assess success, output validity, reproducibility and execution time using consistent resources and timing rules. No automated hidden-test scoring is used.

Report missing data, environment issues or unclear instructions to the event technical support team. Submission deadline: **8 November 2026 at 18:00 WAT (UTC+1)**. Notebook execution is limited to 30 minutes on consistent organiser hardware. See the [Submission Guide](submission-guide.md) for the approved API policy and Track 2 review rubric.
