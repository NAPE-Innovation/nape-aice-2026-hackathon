# Evaluation approach

The final score has three components:

| Component | Weight |
| --- | ---: |
| Presentation judging | 40% |
| Open-test prediction results | 40% |
| Organiser-run inference / reproducibility | 20% |

NAPE scores the submitted `predictions.csv` against the reference answers held privately by organisers. Track 1 uses the numeric curve scorer. Track 2 uses human review of all 32 questions under the [published rubric](../docs/submission-guide.md): the reviewed question total /32 × 40 gives the prediction component. Automated text matching is preliminary only. Afterwards, the NAPE technical team independently executes the submitted notebook/code and checks whether it runs, generates a valid output, can be reproduced using the documented instructions and how long execution takes. This is a **reviewer-run assessment**, not an automated hidden-test evaluation.

Teams are not required to execute code live during their presentations. Scores from different challenge tracks use track-specific metrics and should not be compared directly without an agreed normalisation policy.
