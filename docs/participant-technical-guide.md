# Participant Technical Guide — DRAFT

**NAPE AICE 2026 Hackathon | 7–8 November 2026**

This guide supports both tracks. The [Challenge Brief](../challenges/CHALLENGE_BRIEF.md), [Competition Rules](competition-rules.md) and [Submission Guide](../submission/SUBMISSION_GUIDE.md) govern final requirements once approved. Starter notebooks are optional; the final runnable inference solution is mandatory.

## Before coding
1. Confirm your assigned track and inspect the approved data **preloaded on the team laptop**. Do not download or redistribute raw data.
2. Read the track README and CSV template. Preserve target IDs, columns and units.
3. Check installed Python and available packages. Use a local environment where practical.
4. Plan a reproducible baseline before experimenting with larger models.

## Recommended workflow
- Inspect input files and metadata; verify file paths and sample counts.
- Build a minimal baseline that writes a correctly formatted CSV.
- Add preprocessing, models, calibration, retrieval and confidence handling as relevant.
- Train or fit your solution during the hackathon. Save weights, fitted transformers and indexes needed for inference.
- Freeze the solution by the submission deadline; verify it can run on new inputs **without training, fine-tuning, refitting or rebuilding learned artefacts**.
- Run the submission smoke test and review the output CSV.

## Track 1: Log Digitisation
Inputs: log images/PDF, page registry and requested target-depth/curve rows. Starter notebook: [track 1](../starter-kits/track-1/log_digitisation_starter.ipynb). Aim to map image pixels to calibrated depth/curve values, quantify uncertainty and produce a depth-indexed CSV. Do not treat an example baseline as ground truth.

## Track 2: Archive Intelligence
Inputs: PDF/HTML/XML archive documents, document manifest and open questions. Starter notebook: [track 2](../starter-kits/track-2/archive_intelligence_starter.ipynb). Aim to retrieve evidence, answer questions accurately, cite source paths and abstain when unsupported. Hidden evaluation may use unseen questions against the same approved archive.

## Responsible tools and data
- Open-source libraries, public pretrained models and AI coding assistants are allowed subject to final event rules.
- Do not upload source documents or data to external hosted APIs unless explicitly approved.
- Never commit secrets, hidden data or organiser-only materials.
- Disclose material external models, APIs and datasets in your submission README.
- Ask organisers before installing tools requiring network access or administrator permissions.

## Troubleshooting and checks
- Use paths relative to your project rather than hard-coded personal locations.
- Confirm output headers, row identifiers and confidence conventions.
- Ensure saved weights/indexes are included and can be loaded offline if offline evaluation is required.
- Document runtime, hardware assumptions and any permitted network dependencies.

**To be confirmed before release:** Python/runtime version, laptop specifications, preinstalled packages, permitted APIs/network access, data mount path, support contacts and submission deadline.
