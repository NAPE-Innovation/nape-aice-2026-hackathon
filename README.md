# NAPE AICE 2026 Hackathon

**Theme:** Unlocking Dormant Value  
**Dates:** 7–8 November 2026  
**Venue:** Eko Hotel & Suites, Lagos, Nigeria

This repository contains participant resources for six finalist teams. Challenge allocation takes place by witnessed lucky dip at kickoff, with three teams on each track. Approved challenge-specific Volve datasets are available under `data/track_1/` and `data/track_2/`. Teams may also receive preloaded copies if announced by the organisers.

## Start here

1. Read the [Challenge Brief](CHALLENGE_BRIEF.md) for both challenge tracks.
2. Review the [Competition Rules](docs/competition-rules.md) and [Data Access Guide](docs/data-access.md).
3. Read the [Participant Technical Guide](docs/participant-technical-guide.md). Optional starter notebooks are available for [Track 1](starter-kits/track-1/log_digitisation_starter.ipynb) and [Track 2](starter-kits/track-2/archive_intelligence_starter.ipynb).
4. Follow the [GitHub Setup and Team Submission Guide](docs/github-setup-and-submission.md) to clone the repositories, validate your files and submit to your assigned private team repository.
5. Follow the [Submission Guide](docs/submission-guide.md) and [Submission Template](submission/template/README.md).

## Submission at a glance

In **your assigned team GitHub repository**, create a `submission/` folder at the repository root. Put **notebook(s) + `predictions.csv` + `requirements.txt` + `README.md`** inside it, with clear instructions to reproduce your output. The open-test evaluator reads **`submission/predictions.csv`**. The organisers will record your final commit SHA at the deadline. No Docker, CI/CD configuration, API or separate inference script is required. The NAPE technical team will run your submitted code independently after submission; no live execution during presentations is mandatory.

**Final scoring:** presentation **40%**, open-test prediction score **40%**, organiser-run inference/reproducibility **20%**. No automated hidden-test scoring.

## Repository structure

- `CHALLENGE_BRIEF.md` — both challenge descriptions and deliverables
- `docs/` — competition rules, data access and technical guidance
- `starter-kits/track-1/` and `starter-kits/track-2/` — optional notebook starters
- `submission/` — submission templates; validation is in starter notebooks
- `evaluation/` — public explanation of the evaluation approach

**Submission deadline:** 8 November 2026 at 18:00 WAT (UTC+1). **Notebook execution limit:** 30 minutes on the same organiser hardware. See the [Submission Guide](docs/submission-guide.md) for the approved API policy and Track 2 questions/rubric. Do not commit supplied raw datasets, confidential reference answers, private materials or credentials.
