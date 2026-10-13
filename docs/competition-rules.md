# NAPE AICE 2026 Hackathon — Competition Rules

**Status: DRAFT FOR ORGANISER APPROVAL — NOT YET EFFECTIVE**

**Theme:** Unlocking Dormant Value  
**Hackathon:** 7–8 November 2026, Eko Hotel & Suites, Lagos  
**Format:** In-person, approximately 48 hours; official start, submission cut-off and presentations schedule **[TO CONFIRM]**.

These rules apply to all participants once the approved version is issued. The approved [Participation and Data Use Agreement](participation-and-data-use-agreement.md) also applies.

## 1. Eligibility and teams

- Participation is limited to selected finalists who complete required registration and individual agreement acknowledgements.
- Teams comprise **up to three people**. Six finalist teams will participate, including one organiser-assembled team whose members will choose their team name.
- Team membership changes or substitutions require prior organiser approval. Teams must compete only under their assigned team identity.

## 2. Challenge allocation and scope

- Two challenges are available: **Legacy Well Log Digitisation** and **Intelligent Well Archive**.
- At the event opening, challenge allocation will take place by **witnessed lucky dip**, with three teams assigned to each challenge.
- Teams must work on their allocated challenge using the approved, challenge-specific dataset preloaded on their supplied laptop. No participant dataset download is required.
- The approved [Challenge Brief](../challenges/CHALLENGE_BRIEF.md) defines the task, input materials, submission schemas and challenge-specific deliverables.

## 3. Development window and original work

- Teams must build their **challenge-specific solution during the official hackathon window**.
- General-purpose knowledge, open-source packages, pretrained models, coding assistants and reusable non-challenge-specific utilities are allowed, subject to licences and the data-use agreement.
- Prebuilt solutions specifically tailored to the released challenge, externally completed submissions and passing off another person's work as one's own are prohibited.
- Organiser-provided starter materials may be used by all teams on equal terms.

## 4. Mandatory deliverables — both challenges

Every team must submit:
1. The completed **challenge-specific CSV** matching the supplied schema.
2. **Working executable code, notebook or application** implementing the team's approach. **Code is mandatory for both challenges; a CSV-only submission is insufficient.**
3. A **ready-to-run inference pipeline** that accepts organiser-supplied unseen test inputs and produces the required challenge-specific output CSV without training or fitting. Include trained/fine-tuned model weights, fitted preprocessing components, indexes, configurations and any other runtime artefacts needed, where applicable. A model file is not mandatory if the solution uses no trained model, but a runnable inference pipeline is mandatory.
4. A README covering setup, dependencies, execution steps, approach, limitations, external tools/models/APIs, attribution and reproducibility.
5. A working demonstration or presentation of the solution, including how its outputs were generated.

For **Legacy Well Log Digitisation**, the required output is a depth-indexed CSV using the supplied template; **LAS submission is not required**. For **Intelligent Well Archive**, the required output is an answers CSV with supporting evidence references. See the challenge brief for authoritative columns and formats.

Submission destination, file/folder naming, exact deadline, demo length and permitted final changes: **[TO CONFIRM]**. All teams must receive the same instructions and deadline.

### Submission freeze and hidden evaluation

- All model training, fine-tuning, fitting, index construction and other preparation of learned or persisted solution artefacts must be completed **before the submission deadline**.
- Hidden evaluation is **inference-only**. Organisers must be able to load the submitted frozen solution and run unseen test inputs without retraining, fine-tuning, refitting or rebuilding learned components.
- For Track 1, the solution must process unseen log-image inputs and generate the required depth-indexed CSV. For Track 2, the solution must answer unseen questions against the approved archive and produce the required answers/evidence CSV; unseen documents are not automatically required.
- The precise invocation command, input packaging, allowed runtime preprocessing, execution environment, runtime limits and any API/network access will be specified uniformly to all teams **[TO CONFIRM BEFORE RELEASE]**. Ordinary per-input inference preprocessing is allowed; training or refitting on hidden inputs is not.

## 5. AI, APIs, compute and data handling

- Open-source libraries, public pretrained models and AI coding assistants are permitted.
- Use of paid APIs, external hosted models, internet services, personal hardware and external compute is subject to the event's **approved resource/fairness policy [TO CONFIRM]**.
- Do **not** upload provided raw datasets or documents to external services without express organiser approval and confirmation of applicable dataset permissions.
- Disclose substantial third-party components, model providers, API use and external datasets in the README and presentation.
- Fabricated evidence, invented source citations, falsified outputs and undisclosed external assistance are prohibited.
- Credentials and API keys must not be included in submitted code or published repositories.

## 6. Evidence, quality and reproducibility

- Outputs should be traceable to the approved dataset. Teams should report uncertainty and limitations rather than invent unsupported answers.
- Submitted code must reasonably reproduce the required outputs in the provided environment, with documented dependencies and execution instructions.
- The organisers may evaluate submissions using questions or test cases not shared with teams in advance. Internal answer keys, ground truth, scoring tools and evaluation details are confidential.

## 7. Mentors, conduct and fairness

- Teams may consult officially designated mentors under equivalent access arrangements. Mentors must not write a team's solution or provide confidential judging information.
- Respect other participants, volunteers, sponsors and venue staff. Harassment, intimidation, tampering with other teams' work, cheating or attempts to bypass access controls are prohibited.
- Report equipment, dataset or accessibility problems promptly. Organisers should record and communicate any material clarifications or rule changes to **all teams**.

## 8. Judging and awards

Judging will consider the published criteria, including solution quality, accuracy, evidence, reproducibility, technical execution and practical relevance. **Exact scoring weights, judge composition, tie-breaks, appeals procedure and prize eligibility [TO CONFIRM AND PUBLISH BEFORE COMPETITION].** Judges must declare material conflicts of interest. Organisers may conduct technical validation before final decisions.

## 9. Rule breaches and disputes

The organisers may request clarification, inspect submitted materials and investigate suspected breaches. Responses may include correction requests, score adjustments or disqualification, depending on severity and fairness. The organiser's approved appeals and final decision process **[TO CONFIRM]** applies. Immediate access restrictions may be used for safety or security concerns.

## 10. Publication checklist

Before these rules are final, confirm and publish: eligibility/age requirements; event timetable and submission cut-off; permitted APIs, external compute and device policy; dataset licence and attribution; exact deliverables and submission route; judging rubric and prizes; tie-break and appeal process; participant privacy notice; and approved agreement wording.

**The GitHub-approved versions of these rules, the agreement and challenge brief are the authoritative documents. Google Drive working briefs are not controlling where they differ.**
