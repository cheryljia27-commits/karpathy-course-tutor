# Evaluation

## Question

```text
Does this message help the learner re-enter the right learning loop with less
friction?
```

## Deterministic CLI checks

| Check | Pass condition |
| --- | --- |
| Right re-entry | Names the current focus or unresolved loop |
| Artifact | Assigns one durable object to produce or change |
| Verification | Includes an observable completion check |
| Timebox | Fits a 5–15 minute re-entry by default |
| Source | Points back to a primary public source |
| Low bandwidth | Does not turn the message into the classroom |
| No persona | Does not invent quotes, reactions, or private authority |

The CLI implements these as transparent message invariants, not as a model
quality score. The checks are intentionally simple enough to inspect in
`src/karpathy_course_tutor/engine.py`.

## Labels

| Label | Meaning |
| --- | --- |
| `pass` | Specific, low-bandwidth, source-grounded, and artifact-oriented |
| `soft-pass` | Useful but missing a minor constraint such as a clear timebox |
| `fail` | Generic, wrong-loop, source-free, artifact-free, or persona-like |

## Implemented failure taxonomy

| Failure | Meaning |
| --- | --- |
| `wrong-re-entry` | Chooses a stale or unrelated thread |
| `no-artifact` | Leaves the learner with more conversation but no object |
| `missing-timebox` | Makes the return step feel unbounded |
| `missing-source` | Uses source flavor without an evidence anchor |
| `too-heavy` | Attempts to teach the whole subject in the message |
| `persona-risk` | Simulates identity or invents what the teacher would say |
| `no-verification` | Gives advice without an observable pass/fail check |

## Qualitative review risks

Two useful review risks are not mechanically scored in `v0.1.0`:

| Risk | Meaning |
| --- | --- |
| `performative-memory` | Mentions history to signal intimacy, not to select work |
| `engagement-maxxing` | Asks questions mainly to keep the conversation going |

## Golden-set rule

Do not judge a tutor by whether a message sounds intelligent. Maintain a small
set of learner states, candidate messages, expected labels, and reasons. Add a
row whenever a real failure exposes a missing rule.

The public repository begins with three seed cases in
`examples/eval-set.json`. They demonstrate the evaluation shape; they are not a
claim of broad model-behavior coverage.
