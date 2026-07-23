# Architecture

## Loop

```text
primary source + Obsidian note
  → explicit learner state
  → scheduled morning / evening trigger
  → one iMessage re-entry point
  → optional learner reply
  → one brief follow-up
  → desktop note artifact
  → observable check and state update
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
  "current_note_path": "notes/deep-dive-llms.md",
  "next_artifact": "Rewrite one sentence",
  "completion_check": "The sentence names the action and returned evidence.",
  "timebox_minutes": 10
}
```

Private state is deliberately kept outside the repository.

### Deterministic core

The Python package validates state shape and track values, resolves sources,
previews a low-bandwidth message, records completed artifacts, and evaluates
transparent message invariants. It has no runtime dependency on a model
provider, does not perform adaptive source selection, and does not send
iMessages. It is the public verification layer, not the private proactive
runtime.

### Agent skill

The skill is the adaptive reasoning layer. It can interpret messy notes,
reduce a broad question to one bottleneck, select a source or source segment,
choose an appropriate artifact, and review the result. The skill must preserve
the same source and evaluation boundaries as the deterministic core.

### Transport

The original private prototype used scheduled triggers and an iMessage
read/send bridge. It read the current state and raw Obsidian course note before
choosing a morning or evening anchor. If the learner replied inside the active
window, it sent one brief follow-up and stopped.

Transport remains replaceable in the public architecture. The core can sit
behind:

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
