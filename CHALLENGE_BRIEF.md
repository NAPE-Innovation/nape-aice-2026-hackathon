# NAPE AICE 2026 Hackathon — Participant Challenge Brief

**Theme:** Unlocking Dormant Value  
**Dates:** 7–8 November 2026 | **Venue:** Eko Hotel & Suites, Lagos  
**Duration:** 48 hours | **Status:** Draft — technical review pending

## Why this matters
Decades of subsurface records contain information that can inform energy decisions, but historical well logs and technical documents are often difficult to search, analyse or integrate into modern workflows. Your mission is to transform dormant information into useful, verifiable digital assets.

Six finalist teams will be allocated to two challenge tracks (three per track) by a witnessed random draw at the hackathon kickoff.

## Data and access
The challenges use curated materials from the publicly released **Volve Field** dataset. The approved, challenge-specific dataset will be **preloaded onto the laptop provided to your team**. No dataset download is required. See [Data access](docs/data-access.md) for event-day access instructions. Use only the **approved participant release** for your assigned challenge. Organiser-only references, withheld numerical ground truth and evaluation questions are not available to participants.

### Dataset attribution and licensing

**Source acknowledgement:** The challenge materials are curated from Equinor's publicly released **Volve Field dataset**. Equinor and the relevant Volve licence partners retain their applicable rights in the source material. See [Equinor's Volve data-sharing page](https://www.equinor.com/energy/volve-data-sharing) and [Volve data licence terms](https://cdn.equinor.com/files/h61q9gi9/global/de6532f6134b9a953f6c41bac47a0c055a3712d3.pdf?equinor-hrs-terms-and-conditions-for-licence-to-data-volve.pdf=). Equinor is not represented as sponsoring or endorsing this event. Participants must retain applicable source notices and comply with the approved event data-use agreement.

## Challenge 1 — Legacy Well Log Digitisation

### Problem
Historical logs preserved as raster images or PDFs are not directly usable as numerical depth-indexed curves. Manual digitisation is slow, and depth calibration, curve identification and poor image quality introduce uncertainty.

### Mission
Build an automated or semi-automated solution to recover accurate curve values at specified depths from supplied log images.

### Supplied materials
Relevant log image pages/combined PDF, page registry and metadata, and a depth/curve target template.

### Required deliverables
1. **Completed depth-indexed CSV** using the supplied `target_depths_template.csv` with columns `page_id,well,depth_m,curve,value,confidence,notes`. Preserve the target identifiers and depth/curve combinations. **LAS output is not required.**
2. **Working solution:** reproducible code, notebook or application showing how the values were produced.
3. **Technical README:** setup and execution steps; image preprocessing; curve identification; depth/value calibration; QC and confidence; assumptions, failure modes and limitations.
4. **Demonstration:** show extraction on representative images, quality checks and practical use of the resulting numerical data.
5. **Reproducible notebook:** include any required model or calibration artefacts (where applicable), `requirements.txt`, and clear instructions so NAPE reviewers can independently run the submitted notebook and regenerate the CSV.

A strong solution will demonstrate extraction accuracy, appropriate depth registration, reproducibility and honest uncertainty reporting. Optional enhancements (batch processing, interactive QC, LAS export) cannot replace the CSV.

## Challenge 2 — Intelligent Well Archive

### Problem
Technical and drilling information is scattered across historical PDF, HTML, XML and related records. Finding trustworthy answers manually can be slow, and unsupported answers can mislead users.

### Mission
Build a workflow that finds and answers technical questions from the supplied archive, with verifiable document evidence and appropriate uncertainty handling.

### Supplied materials
Curated archive documents, document metadata/manifest and an answers template.

### Required deliverables
1. **Completed answers CSV** following the supplied template with columns `question_id,answer,evidence,confidence,notes`. Evidence should identify supporting document paths or references.
2. **Working solution:** reproducible code, notebook or application showing document processing, retrieval and/or extraction and answer generation.
3. **Technical README:** setup and execution steps; document handling; retrieval/extraction; evidence provenance; confidence, ambiguity and unsupported-answer handling; limitations.
4. **Demonstration:** answer representative questions and show where the evidence comes from.
5. **Reproducible notebook:** include any required saved indexes, models and configurations (where applicable), `requirements.txt`, and clear instructions so NAPE reviewers can independently run the submitted notebook and regenerate the CSV.

### Practice questions and evaluation
An **open question set** will be provided for development and testing. The final open question set and answer-template IDs will be confirmed in the approved release. Solutions should derive answers from the archive rather than relying on hard-coded answers. The evaluation procedure and final submission instructions will be communicated by organisers.

A strong solution will return accurate, evidence-supported answers and recognise when the supplied archive does not justify an answer. Optional semantic search, RAG, interfaces and visualisations are welcome but not required.

## Technical evaluation expectations

**Challenge 1:** Solutions will be assessed for curve-value extraction quality, correct depth registration and calibration, reproducibility, and transparent QC/uncertainty handling. Submitted open-test predictions will be scored against organiser-held reference answers; additional judging is described below.

**Challenge 2:** Solutions will be assessed for answer correctness, relevance and traceability of document evidence, handling of ambiguity or unsupported questions, and reproducibility. Submitted open-test answers will be scored against organiser-held reference answers; additional judging is described below.

## Final scoring

- **Presentation judging:** 40%.
- **Open-test CSV accuracy/quality:** 40%.
- **Organiser-run inference and reproducibility:** 20% (execution success, valid output, reproducibility, runtime).

Teams submit notebook(s), `predictions.csv`, `requirements.txt`, and a `README.md`. A separate inference script, API, Docker image and CI/CD setup are not required.

## Requirements applying to both challenges
- Use the approved participant dataset for challenge-specific evidence.
- Submit the required CSV **and** a working, explainable solution; a CSV alone is insufficient.
- Provide source files, dependencies, run instructions, methodology, assumptions and limitations.
- Disclose external services and models used; follow final event rules on APIs and data handling.
- Present and explain the solution during judging; live notebook execution is not required.
- Do not seek access to organiser-only reference/evaluation materials.
- NAPE technical reviewers will independently execute the submitted notebook/code after handover using the supplied instructions and consistent resources. There is no automated hidden-test scoring.
- Submission packaging, channel, deadline and execution instructions are maintained in the separate [Submission Guide](submission/SUBMISSION_GUIDE.md). The [Competition Rules](docs/competition-rules.md) govern permitted tools, external services, conduct and fairness. The approved judging rubric governs scores and tie-breaks.

**Goal:** Unlock existing data, reveal reliable insights and demonstrate practical value for subsurface workflows.
