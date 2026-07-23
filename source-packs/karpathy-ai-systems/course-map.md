# Karpathy AI systems course map

This source pack is an original navigation and learning layer over primary
public material. It contains no transcripts and makes no claim of affiliation.

## Track 1 — LLM systems

Question:

> What is an LLM as a system?

| Source | Priority | Learning move | Minimum artifact |
| --- | --- | --- | --- |
| [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI) | P0 | Separate mechanisms, capabilities, and limitations | One mechanism → behavior → product-risk row |
| [Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g) | P0 | Build a system-level mental model first | Map parameters, context, tools, and failures |
| [How I use LLMs](https://www.youtube.com/watch?v=EWvNQjAaOHw) | P0 | Connect behavior to a real human workflow | Task → model role → verification table |
| [Building micrograd](https://www.youtube.com/watch?v=VMj-3S1tku0) | P0 | Build the smallest complete mechanism | Trace one value and gradient by hand |
| [Let's build GPT](https://www.youtube.com/watch?v=kCc8FmEb1nY) | P0 | Grow from a tiny baseline to a Transformer | Trace one token through one block |
| [Let's build the GPT Tokenizer](https://www.youtube.com/watch?v=zduSFxRajkE) | P1 | Turn preprocessing into inspectable edge cases | Compare three tokenizations |
| [Let's reproduce GPT-2](https://www.youtube.com/watch?v=l8pRSuU81PU) | P1 | Use reproduction and checkpoints as evidence | Assumption → observable → checkpoint list |
| [LLM101n (archived course proposal)](https://github.com/karpathy/LLM101n) | P1 | Frame an end-to-end AI-system curriculum | Raw data → evaluated behavior map |

## Track 2 — Agent and tutor loops

Question:

> What is the smallest complete learning or agent loop?

| Source | Priority | Learning move | Minimum artifact |
| --- | --- | --- | --- |
| [Software Is Changing (Again)](https://www.youtube.com/watch?v=LCEmiRjPEtQ) | P0 | Separate software layers and interfaces | 1.0 / 2.0 / 3.0 boundary table |
| [LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) | P0 | Make files a compounding source of truth | Raw source → compiled note → context map |
| [The append-and-review note](https://karpathy.bearblog.dev/the-append-and-review-note/) | P0 | Prefer a small knowledge loop over a large system | One append-only note and review rule |
| [autoresearch](https://github.com/karpathy/autoresearch) | P1 | Constrain an agent around a measurable loop | State → action → metric → stop rule diagram |

## Track 3 — Evaluation and verification

Question:

> How do we know the tutor or model loop is working?

| Source | Priority | Learning move | Minimum artifact |
| --- | --- | --- | --- |
| [A Recipe for Training Neural Networks](https://karpathy.github.io/2019/04/25/recipe/) | P0 | Verify a baseline before adding complexity | Baseline → failure → hypothesis → check row |
| [Verifiability](https://karpathy.bearblog.dev/verifiability/) | P0 | Compare generation cost with checking cost | Verification-cost table for three tasks |

## Progress rule

Do not measure progress by hours watched. Measure it by durable artifacts:

- a mechanism note;
- a toy implementation;
- a trace or diagram;
- an eval row;
- a failure taxonomy;
- a source-backed product decision.

Stop a session when one useful artifact exists. Do not continue merely to
finish a video.

## Source policy

- Prefer creator-owned pages, repositories, and channels.
- Use third-party transcripts only as navigation aids and verify against the
  primary source.
- Distinguish a direct source claim from an inferred teaching pattern.
- Never fabricate a quotation or attribute the tutor's advice to Karpathy.
