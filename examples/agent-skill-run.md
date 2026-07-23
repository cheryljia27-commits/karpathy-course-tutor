# Representative Agent Skill run

This is a public, anonymized run produced from the bundled
`karpathy-course-tutor` Agent Skill. It demonstrates the adaptive layer without
publishing private notes or message history.

## Input

```json
{
  "current_track": "llm-systems",
  "current_source_id": "deep-dive-llms",
  "focus": "tool use and web search",
  "open_loop": "Explain what the model checked, not only what tool use does.",
  "next_artifact": "Rewrite one sentence in notes/tool-use.md",
  "completion_check": "The sentence names both the external action and the returned evidence.",
  "timebox_minutes": 10,
  "stuck_point": "The note describes the feature but not the mechanism.",
  "avoid_today": [
    "restart the whole lecture",
    "collect more sources"
  ],
  "history": []
}
```

## Agent decision

- Keep the current primary source because the unresolved loop is still inside
  its tool-use section.
- Do not restart the lecture or gather more material; neither action makes the
  missing mechanism observable.
- Convert the vague goal into one durable sentence with a binary completion
  check.

## Output

```text
Re-entry: Explain what the model checked, not only what tool use does.
Artifact: Spend 10 minutes rewriting one sentence in notes/tool-use.md.
Check: Pass if the sentence names both the external action and the returned evidence.
Source: Deep Dive into LLMs like ChatGPT
        https://www.youtube.com/watch?v=7xTGNNLPyMI
```

## Observable result

Example artifact:

> The model sends a web-search query, receives external results, and uses the
> returned evidence to support or revise its answer.

Result: **pass**. The sentence names both the external action and the returned
evidence, stays inside the ten-minute scope, and can be saved back to the
learner's notes.

This run is intentionally small. It demonstrates state selection and artifact
verification, not a claim that one intervention proves end-to-end tutor
quality.
