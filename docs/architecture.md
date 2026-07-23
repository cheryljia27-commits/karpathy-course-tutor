# Architecture

## Loop

```text
primary source
  → learner state
  → re-entry selection
  → small artifact
  → observable check
  → state update
  → next re-entry
```

## Layers

### Source pack

The source pack contains official URLs, bibliographic metadata, original
teaching-move summaries, and minimum artifacts. It does not contain full
transcripts or scraped course material.

### Learner state

The learner state is an explicit JSON file. It stores only what is useful for
selecting the next intervention:

```json
{
  "current_track": "llm-systems",
  "current_source_id": "deep-dive-llms",
  "focus": "tool use and web search",
  "open_loop": "Explain what the model checked.",
  "next_artifact": "Rewrite one sentence",
  "completion_check": "The sentence names the action and returned evidence.",
  "timebox_minutes": 10
}
```

Private state is deliberately kept outside the repository.

### Deterministic core

The Python package validates state, resolves sources, previews a low-bandwidth
message, records completed artifacts, and evaluates message invariants. It has
no runtime dependency on a model provider.

### Agent skill

The skill is the adaptive reasoning layer. It can interpret messy notes,
reduce a broad question to one bottleneck, choose an appropriate artifact, and
review the result. The skill must preserve the same source and evaluation
boundaries as the deterministic core.

### Transport

Transport is replaceable. The original prototype used iMessage, but the core
can sit behind:

- a local scheduled command;
- an agent runtime;
- a notification service;
- a messaging integration;
- a manual study-session prompt.

Separating transport prevents phone-specific or account-specific code from
becoming part of the learning model.

## Trust boundary

```text
source claims       → cite a primary source
teaching synthesis  → label as an interpretation
learner state       → keep local and minimal
model output        → verify through an artifact or observable check
```
