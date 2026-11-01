# GitHub Setup and Team Submission Guide — NAPE AICE 2026

**The shared hackathon repository is for resources. Your assigned private team repository is the official submission location.** The organisers will evaluate the final version on your team's `main` branch at the announced deadline.

## Before you begin

- Create a GitHub account and send your **exact GitHub username** to the organisers.
- Install Git and Python/Jupyter as needed.
- Accept invitations to the shared resources repository and your team's private repository. If cloning a private repository prompts for authentication, sign in using GitHub CLI (`gh auth login`), Git Credential Manager or an SSH key; a GitHub account password cannot be used as an HTTPS Git password.

## 1. Clone the shared resources repository

```bash
git clone https://github.com/NAPE-Innovation/nape-aice-2026-hackathon.git
cd nape-aice-2026-hackathon
```

Read `CHALLENGE_BRIEF.md`, `submission/SUBMISSION_GUIDE.md`, and the starter notebook for your assigned track. The approved dataset is in `data/track_1/` or `data/track_2/`. **Do not push solutions into this shared repository.**

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

The validator lives in the **shared hackathon repository**, but you point it to the `submission/` folder inside **your team repository**.

Assume you cloned both repositories into the same parent folder:

```text
hackathon-work/
├── nape-aice-2026-hackathon/       # shared resources and validator
└── nape-aice-2026-pipeline-x/      # example team repository
    └── submission/
        ├── solution.ipynb
        ├── predictions.csv
        ├── requirements.txt
        └── README.md
```

**Example for a Track 1 team:** from the **shared repository root**:

```bash
cd ../nape-aice-2026-hackathon
python submission/validate_submission.py --track 1 --submission ../nape-aice-2026-pipeline-x/submission
```

**Example for a Track 2 team:** run the same command with `--track 2`:

```bash
python submission/validate_submission.py --track 2 --submission ../nape-aice-2026-pipeline-x/submission
```

Use your own team folder in place of `nape-aice-2026-pipeline-x`. A valid submission returns a JSON report with `"valid": true` for both `structure` and `csv`. If validation fails, read the `errors` fields, correct your files and rerun the command. **This does not check prediction accuracy or execute your notebook.**

Prediction CSV headers must be:

- **Track 1:** `page_id,well,depth_m,curve,value,confidence`
- **Track 2:** `question_id,answer,evidence,confidence`

Use the track-specific CSV template supplied in `submission/template/outputs/`. The file must contain your actual predictions, not just the header.

## 6. Official submission

**Your assigned team repository is your submission.** Push the final `submission/` folder to the team's `main` branch before the official deadline. The organisers will record the final commit SHA and assess that version. No separate email or Drive upload is required unless the organisers explicitly announce a contingency.

Before the deadline, check `git status` for uncommitted work, `git push origin main` for successful upload, and GitHub's web interface for the latest files. Do not commit API keys, secrets, raw supplied datasets or confidential reference answers.

**Submission deadline:** To be announced by the organisers.

For the full format and scoring requirements, see [Submission Guide](../submission/SUBMISSION_GUIDE.md).
