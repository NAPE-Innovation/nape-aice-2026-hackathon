# Submission Guide and Inference Contract — DRAFT

**Applies to both challenge tracks.** See [Competition Rules](../docs/competition-rules.md) and the [Challenge Brief](../CHALLENGE_BRIEF.md). This guide defines the proposed common submission format; the exact command and runtime will be confirmed before release.

## Mandatory deliverables
1. Completed challenge-specific predictions CSV using the supplied schema.
2. Working source code/notebook/application **and a runnable inference entry point**.
3. Frozen trained model weights, fitted preprocessing, embeddings/indexes and configuration **where applicable**.
4. README with setup, run command, dependencies, data paths, architecture, methodology, licences, limitations and external services.
5. Demonstration/presentation.

**A CSV alone is insufficient. A model file alone is insufficient.** Teams that do not train a model still submit an inference-ready pipeline.

## Proposed submission layout

```text
team-x/
├── README.md
├── requirements.txt
├── run_inference.py
├── src/                     # optional
├── models/                  # weights/fitted artefacts if applicable
├── indexes/                 # persisted retrieval indexes if applicable
└── outputs/
    └── predictions.csv
```

The submission root folder must match the team's registered name in lowercase, with spaces replaced by hyphens (for example, **Team X** → `team-x/`, **Team Alpha** → `team-alpha/`). Keep the organiser-assigned team ID separately for submission confirmation and scoring. Do not rename the submission folder after the final handover. This naming convention is proposed pending approval of the overall submission mechanism.

## Proposed common invocation

```bash
python run_inference.py --input /path/to/test_input --output /path/to/predictions.csv
```

The `--input` path may point to a directory or CSV according to the track. The command must write the CSV at `--output`, return a nonzero exit code on failure, and not require interactive prompts. The supplied [Python template](template/run_inference.py) illustrates the command-line contract; it deliberately does not generate predictions.

### Track 1
The test input contains new log images and target-depth/curve requests. Output columns: `page_id,well,depth_m,curve,value,confidence,notes`. Preserve requested identifiers. LAS is not required.

### Track 2
The test input contains a question CSV and refers to the approved archive. Output columns: `question_id,answer,evidence,confidence,notes`. Evidence must reference the supporting archive documents. Hidden questions may be unseen even when the documents are familiar.

## Freeze and evaluation
- **Complete all training, fine-tuning, fitting and index construction before submission.**
- Organisers will run the submitted frozen solution on unseen inputs. No training, refitting, index rebuilding or retrieval of hidden answers is allowed during evaluation.
- Ordinary deterministic preprocessing of each unseen input is permitted.
- The organisers may verify execution independently. Do not rely on team members manually editing predictions during evaluation.
- The permitted network/API policy, hardware/runtime limits, input folder schema, scoring tolerances and exact entry-point convention **remain to be confirmed**.

## Pre-submit checks
- Can the command run from a clean shell with documented dependencies?
- Are all required model and index artefacts present and loadable?
- Does the CSV exactly match the challenge-specific schema?
- Are data references and evidence paths valid?
- Are credentials, organiser-only data and hidden reference files excluded?
- Does the README accurately describe third-party components and licence obligations?

## Self-validation (participant-facing)

You can check both the submission package structure and your CSV without access to reference answers:

```bash
python submission/validate_submission.py --track 1 --submission /path/to/team-submission
# Use --track 2 for archive intelligence
```

Or import the checks:

```python
from submission.validate_submission import validate_csv, validate_structure
print(validate_csv("team-submission/outputs/predictions.csv", "1"))
print(validate_structure("team-submission"))
```

This checks required files, CSV columns, identifiers, basic numeric fields and confidence range. It **does not** check prediction accuracy, hidden answers, inference execution or model quality. The proposed submission layout remains subject to final event runtime confirmation.

## Two-stage technical evaluation

**Stage 1 — open-test CSV:** organisers score the submitted CSV against the corresponding open-test reference. **Stage 2 — hidden inference:** organisers run each team's frozen inference code on unseen inputs, then score the generated CSV against separate restricted hidden references. The same track-specific metric can be used for both stages; results should remain separate until final judging weights are approved.
