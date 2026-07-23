# Learner-state schema

Use the minimum state needed to select one next intervention.

```json
{
  "current_track": "llm-systems",
  "current_source_id": "deep-dive-llms",
  "focus": "tool use and web search",
  "open_loop": "Explain what the model checked.",
  "stuck_point": "The note describes the feature, not the mechanism.",
  "current_note_path": "notes/deep-dive-llms.md",
  "next_artifact": "Rewrite one sentence",
  "completion_check": "The sentence names the action and returned evidence.",
  "timebox_minutes": 10,
  "avoid_today": ["restart the whole lecture"],
  "history": []
}
```

## Field rules

- `current_track`: one of `llm-systems`, `agent-loops`, or `evaluation`.
- `current_source_id`: stable id from the course map.
- `focus`: a narrow concept, mechanism, or product decision.
- `open_loop`: the exact unresolved claim or question.
- `stuck_point`: optional evidence about why the loop remains open.
- `current_note_path`: optional path to the learner's current durable note.
- `next_artifact`: one durable object, not “study” or “think more.”
- `completion_check`: one observable condition that can pass or fail.
- `timebox_minutes`: normally 5–15 for re-entry.
- `avoid_today`: tempting work that would increase scope without resolving the
  loop.
- `history`: keep only completed artifacts and useful reflections.

If state is missing, infer a provisional version from the learner's note and
mark the inference. Ask only for the one missing fact that would materially
change the next artifact.
