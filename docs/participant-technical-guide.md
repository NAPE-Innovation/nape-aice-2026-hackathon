# Participant Technical Guide — Review Draft

**NAPE AICE 2026 Hackathon | 7–8 November 2026 | Both tracks**

This guide explains the technical workflow. The [Challenge Brief](../challenges/CHALLENGE_BRIEF.md) defines the challenges, the [Competition Rules](competition-rules.md) govern participation and permitted tools, and the [Submission Guide](../submission/SUBMISSION_GUIDE.md) defines submission expectations. Starter notebooks are **optional teaching aids, not finished solutions**.

## 1. Your environment and approved data

- Use your assigned track's **approved participant dataset preloaded on the organiser-provided team laptop**. No download of the raw dataset is required.
- Locate the dataset using the event-day path supplied by technical support. Example paths in notebooks are placeholders; do not assume the actual directory structure is identical.
- Check the manifest, available inputs and template before processing. Do not access organiser-only references, hidden questions or withheld ground truth.
- Do not upload raw challenge data or documents to hosted AI services, personal storage or external APIs unless the organisers explicitly approve that processing and confirm dataset permissions.
- Do not commit raw data, access credentials or secrets to repositories.

## 2. Before you build

1. Confirm your track, dataset path and the files listed in the supplied manifest.
2. Inspect the required CSV template and preserve the exact column names and requested identifiers.
3. Check Python, installed dependencies, available disk space and whether approved network/API access is working.
4. Run the optional track notebook to inspect sample inputs. Missing paths should be resolved with technical support; do not silently invent input data.
5. Start with a minimal reproducible workflow and document assumptions and limitations.

## 3. Track 1 — Legacy Well Log Digitisation

**Inputs:** approved log images/PDFs, page registry/metadata and target-depth/curve template. [Starter notebook](../starter-kits/track-1/log_digitisation_starter.ipynb).

**Required output columns:** `page_id,well,depth_m,curve,value,confidence,notes`.

Build image/page identification, depth and curve calibration, extraction, QC and uncertainty handling. The starter notebook only previews inputs and checks the output contract; it does **not** implement OCR, calibration or curve extraction. Preserve target identifiers and row coverage. LAS is optional, not a substitute for the CSV.

## 4. Track 2 — Intelligent Well Archive

**Inputs:** approved archive documents, document manifest and open questions/answer template. [Starter notebook](../starter-kits/track-2/archive_intelligence_starter.ipynb).

**Required output columns:** `question_id,answer,evidence,confidence,notes`.

Build document parsing, retrieval or extraction, answer generation and evidence tracing. Cite approved source paths and abstain where the archive does not support an answer. The starter notebook demonstrates local inspection and a simple keyword-search baseline; it does **not** provide a complete PDF pipeline or answer-generation system. Hidden evaluation may use unseen questions against the approved archive.

## 5. Freeze your solution for unseen-input evaluation

- Build, train, fine-tune, fit, calibrate and create persisted retrieval indexes **during the hackathon, before submission**.
- Save model weights, fitted transformers, indexes, calibration settings and other required artefacts, where applicable.
- Submit a non-interactive runnable inference entry point that loads these frozen artefacts and produces the track-specific CSV for unseen inputs.
- Hidden evaluation is **inference-only**: no retraining, refitting or rebuilding learned/persisted artefacts on hidden inputs. Ordinary per-input preprocessing is allowed.
- A CSV-only submission is insufficient. A trained model file is not mandatory if no model is trained, but a runnable inference workflow is mandatory.
- The common proposed command is `python run_inference.py --input <test_input> --output <predictions.csv>`. Follow the final [Submission Guide](../submission/SUBMISSION_GUIDE.md) if this convention is revised.

## 6. Pre-submission checks

- Output has the exact track-specific headers, requested identifiers and expected row coverage.
- Evidence references (Track 2) point to approved archive sources; unsupported claims are not fabricated.
- Confidence values and missing/uncertain outputs are documented consistently.
- A fresh process can load saved artefacts and produce predictions without interactive notebook state.
- Dependencies, input paths, runtime assumptions, licences, external tools and APIs are documented in the README.
- No credentials, raw supplied data or organiser-only material are bundled in the submission.
- A team member can explain and demonstrate the workflow and limitations.

## 7. Support and release-day confirmations

Report missing data, corrupt files, environment problems or suspected data exposure promptly to the event technical helpdesk. Material clarifications will be shared with all teams.

**Pending organiser confirmation before participant release:** actual laptop specifications and Python version; installed packages; data root/mount paths; permitted external API/network and compute policy; available credentials and quotas; final inference command and input packaging; runtime limits; submission deadline/channel; technical support contact.

**Note:** The notebooks intentionally do not generate final predictions. Teams are responsible for their own solutions and runnable inference pipelines.
