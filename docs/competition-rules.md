# NAPE AICE 2026 Hackathon — Competition Rules

**Status: Approved by Promise E.**

**Theme:** Unlocking Dormant Value  
**Hackathon:** 7–8 November 2026, Eko Hotel & Suites, Lagos  
**Format:** In-person, approximately 48 hours.

These rules apply to all participants. The approved Participation and Data Use Agreement also applies.

## 1. Eligibility and teams

- Participation is limited to selected finalists who complete required registration and individual agreement acknowledgements.
- Teams comprise **up to three people**. Six finalist teams will participate, including one organiser-assembled team whose members will choose their team name.
- Team membership changes or substitutions require prior organiser approval. Teams must compete only under their assigned team identity.

## 2. Challenge allocation and scope

- Two challenges are available: **Legacy Well Log Digitisation** and **Intelligent Well Archive**.
- At the event opening, challenge allocation will take place by **witnessed lucky dip**, with three teams assigned to each challenge.
- Teams must work on their allocated challenge using the approved, challenge-specific dataset preloaded on their supplied laptop. No participant dataset download is required.
- The approved [Challenge Brief](../CHALLENGE_BRIEF.md) defines the task, input materials, submission schemas and challenge-specific deliverables.

## 3. Development window and original work

- Teams must build their **challenge-specific solution during the official hackathon window**.
- General-purpose knowledge, open-source packages, pretrained models, coding assistants and reusable non-challenge-specific utilities are allowed, subject to licences and the data-use agreement.
- Prebuilt solutions specifically tailored to the released challenge, externally completed submissions and passing off another person's work as one's own are prohibited.
- Organiser-provided starter materials may be used by all teams on equal terms.

**Submission deadline: 8 November 2026 at 18:00 WAT (UTC+1).** Submit to the assigned private repository before the cutoff. Organisers record the final commit and evaluate that version.

## 4. Mandatory deliverables — both challenges

Every team must submit:
1. A completed **challenge-specific `predictions.csv`** matching the supplied template.
2. **One or more Jupyter notebooks (`.ipynb`)** containing the submitted solution.
3. A **`requirements.txt`** identifying the Python packages needed to run the solution.
4. A **`README.md`** with setup instructions, input paths, steps to run the notebook and reproduce the CSV, external services, attribution, assumptions and limitations.
5. A presentation explaining the approach and results.

Any saved model weights, indexes or configuration needed for reproduction must also be provided or clearly documented where applicable. No separate `run_inference.py` script, Docker image, API or CI/CD setup is required. Teams are **not required to run their notebooks live** during presentations.

Track 1 output: depth-indexed CSV using the published columns; LAS is optional. Track 2 output: answers CSV including evidence references. See the [Submission Guide](submission-guide.md).

### Independent technical execution

After submission, the NAPE technical team will execute each team's submitted code/notebook using its documented requirements and instructions. Execution success, output validity, reproducibility and runtime will contribute to the inference/reproducibility score. Organisers use the same hardware and a 30-minute notebook execution limit. Approved dependencies are prepared before timing; setup difficulties are recorded separately. There is **no automated hidden-test evaluation**.

## 5. AI, APIs, compute and data handling

- Open-source libraries, public pretrained models and AI coding assistants are permitted.
- Internet access, open-source tools and pretrained models are allowed. Paid APIs require equal organiser-approved access. Official notebook execution uses the same organiser hardware for every team and a 30-minute limit; external compute must not replace that assessment.
- Do **not** upload provided raw datasets or documents to external services without express organiser approval and confirmation of applicable dataset permissions.
- Disclose substantial third-party components, model providers, API use and external datasets in the README and presentation.
- Fabricated evidence, invented source citations, falsified outputs and undisclosed external assistance are prohibited.
- Credentials and API keys must not be included in submitted code or published repositories.

## 6. Evidence, quality and reproducibility

- Outputs should be traceable to the approved dataset. Teams should report uncertainty and limitations rather than invent unsupported answers.
- Submitted code must reasonably reproduce the required outputs in the provided environment, with documented dependencies and execution instructions.
- Open-test reference answers and internal scoring tools remain confidential. Organisers may independently check whether submitted code reproduces its claimed outputs.

## 7. Mentors, conduct and fairness

- Teams may consult officially designated mentors under equivalent access arrangements. Mentors must not write a team's solution or provide confidential judging information.
- Respect other participants, volunteers, sponsors and venue staff. Harassment, intimidation, tampering with other teams' work, cheating or attempts to bypass access controls are prohibited.
- Report equipment, dataset or accessibility problems promptly. Organisers should record and communicate any material clarifications or rule changes to **all teams**.

## 8. Judging and awards

Final scores are allocated as **40% presentation judging, 40% open-test prediction results, and 20% organiser-run inference/reproducibility**. Technical reviewers assess whether the submitted solution executes successfully, produces expected outputs, follows documented instructions and completes within agreed runtime criteria. Judges must declare material conflicts of interest. Organisers may conduct validation before final decisions.

The approved per-question Track 2 rubric, including equivalent answers and abstentions, is in the [Submission Guide](submission-guide.md).

## 9. Rule breaches and disputes

The organisers may request clarification, inspect submitted materials and investigate suspected breaches. Responses may include correction requests, score adjustments or disqualification, depending on severity and fairness.
