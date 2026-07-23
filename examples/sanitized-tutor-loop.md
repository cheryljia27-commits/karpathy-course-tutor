# Sanitized AI Tutor Bot loop

This is the sanitized interaction shown in the original 8.5-second AI Tutor
Bot demo. The private prototype used an explicit learner-state file, the
current Obsidian course note, scheduled triggers, and an iMessage read/send
bridge. Private notes, contact identifiers, and transport credentials are not
included here.

## State before the evening anchor

```json
{
  "current_source_id": "deep-dive-llms",
  "current_section": "tool use and web search",
  "open_loop": "Explain what the model checked, not only what tool use does.",
  "next_artifact": "Rewrite one sentence in the current Obsidian course note",
  "completion_check": "The sentence names the external action and returned evidence.",
  "avoid_today": [
    "restart the whole lecture",
    "turn the phone conversation into the classroom"
  ]
}
```

## Evening anchor

```text
🌙 If you touch the note tonight, stay in the same section.

Tool use and web search are still the loose bit.

One unfinished sentence is enough to leave for tomorrow.
```

Learner:

```text
yeah, leaving that one open
```

Tutor:

```text
That is enough. Leave it there so you can pick it up tomorrow.
```

The evening exchange leaves a handle instead of demanding completion.

## Morning re-entry

```text
☀️ No need to rebuild the plan this morning.

Your note already points back to tool use and web search.

Just rewatch that bit and make one sentence less vague.
```

Learner:

```text
yeah, that part is still fuzzy
```

Tutor:

```text
Good. Make the sentence say what the model checked, not just what tool use does.
```

## Desktop artifact

The learner returns to the primary course and rewrites the note:

> The model sends a web-search query, receives external results, and uses the
> returned evidence to support or revise its answer.

Result: **pass**. The phone owned the moment of re-entry; the source and
Obsidian note still owned the learning. The tutor stopped after one brief
follow-up rather than maximizing conversation.

This is a curated hero path through a real system design. It demonstrates the
intended behavior, not a claim of autonomous production reliability.
