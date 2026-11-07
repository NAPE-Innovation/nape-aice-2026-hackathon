# GitHub Setup and Team Submission Guide — NAPE AICE 2026

**The shared hackathon repository is for resources. Your assigned private team repository is the official submission location.** The organisers will evaluate the final version on your team's `main` branch at the announced deadline.

## Before you begin

- **Sign in to your existing GitHub account or [create an account](https://github.com/signup)**, then send your **exact GitHub username** to the organisers.
- Install Git and Python/Jupyter as needed.
- Accept invitations to the shared resources repository and your team's private repository. If cloning a private repository prompts for authentication, sign in using GitHub CLI (`gh auth login`), Git Credential Manager or an SSH key; a GitHub account password cannot be used as an HTTPS Git password.

## 1. Clone the shared resources repository

```bash
git clone https://github.com/NAPE-Innovation/nape-aice-2026-hackathon.git
cd nape-aice-2026-hackathon
```

Read the [Challenge Brief](../CHALLENGE_BRIEF.md), [Submission Guide](submission-guide.md), [Data Access Guide](data-access.md), and the [Track 1](../starter-kits/track-1/log_digitisation_starter.ipynb) or [Track 2](../starter-kits/track-2/archive_intelligence_starter.ipynb) starter notebook. Data is in [Track 1](../data/track_1/) or [Track 2](../data/track_2/). **Do not push solutions into this shared repository.**

## 2. Clone your assigned private team repository

Each team will receive its own repository URL and access invitation. For example, **Pipeline X** would run:

```bash
cd ..
git clone https://github.com/NAPE-Innovation/nape-aice-2026-pipeline-x.git
cd nape-aice-2026-pipeline-x
```

**Example only:** replace `pipeline-x` with your actual assigned repository name. If you see `Repository not found`, confirm the URL and accept the invitation, then check authentication.

## 3. Develop and organise your submission

You may use the shared starter notebook as a starting point. Copy the notebook into your **team repository** and implement your solution there. Keep raw datasets outside Git; document their expected local paths in your submission README.

Your team repository must contain the following **at its root**:

```text
submission/
├── solution.ipynb       # one or more notebooks; filename can differ
├── predictions.csv      # your track's required output
├── requirements.txt     # Python dependencies
└── README.md            # reproducible run instructions
```

The notebook should be runnable using the approved dataset, with no hard-coded personal paths or embedded credentials. Optional supporting model artefacts may be included if needed for reproduction.

## 4. Commit and push your work

Run these commands **from inside your team repository**:

```bash
git status
git add submission/
git commit -m "Add team solution and predictions"
git push origin main
```

Commit regularly. If your team uses feature branches, merge the final work into `main` before the deadline. Verify the files are visible on GitHub.

## 5. Validate your submission — worked example

The final **Validate Your Submission** section in each starter notebook checks your team's submission folder. For example, if the shared and team repositories are next to each other:

```text
hackathon-work/
├── nape-aice-2026-hackathon/
└── nape-aice-2026-pipeline-x/
    └── submission/
        ├── solution.ipynb
        ├── predictions.csv
        ├── requirements.txt
        └── README.md
```

Open the [Track 1](../starter-kits/track-1/log_digitisation_starter.ipynb) or [Track 2](../starter-kits/track-2/archive_intelligence_starter.ipynb) notebook and in its final validation cell set:

```python
SUBMISSION_DIR = Path("../nape-aice-2026-pipeline-x/submission")
```

Replace `pipeline-x` with your own team name. The path is relative to the notebook's **current working directory**; adjust it as needed. Run the validation cell and correct any reported errors. The check does not execute your solution or score prediction accuracy.

The notebooks use `submission/validate_submission.py` from this repository. You can also run it from a terminal at the repository root:

```bash
python submission/validate_submission.py --track 1 ../nape-aice-2026-pipeline-x/submission
```

Use `--track 2` for Track 2. Errors must be fixed; warnings (for example, targets with no row, which score zero) are for your information.

Prediction CSV headers must be:

- **Track 1:** `page_id,well,depth_m,curve,value,confidence` (optional `notes`). Target depths only, or full extracted logs; only the target depths are scored (nearest submitted depth within 0.10 m).
- **Track 2:** `question_id,answer,evidence,confidence` (optional `notes`)

Use the track-specific CSV template supplied in `submission/template/outputs/`. Both templates list every published target or question, so keep their identifiers and fill in your answers. The file must contain your actual predictions, not just the header.

## 6. Official submission

**Your assigned team repository is your submission.** Push the final `submission/` folder to the team's `main` branch before the official deadline. The organisers will record the final commit SHA and assess that version. No separate email or Drive upload is required unless the organisers explicitly announce a contingency.

Before the deadline, check `git status` for uncommitted work, `git push origin main` for successful upload, and GitHub's web interface for the latest files. Do not commit API keys, secrets, raw supplied datasets or confidential reference answers.

**Submission deadline:** 8 November 2026 at 18:00 WAT (UTC+1).

For the full format and scoring requirements, see [Submission Guide](submission-guide.md).
