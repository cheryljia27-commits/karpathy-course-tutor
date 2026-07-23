from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any


TRACKS = frozenset({"llm-systems", "agent-loops", "evaluation"})


@dataclass(slots=True)
class LearnerState:
    current_track: str
    current_source_id: str
    focus: str
    open_loop: str
    next_artifact: str
    completion_check: str
    timebox_minutes: int = 10
    stuck_point: str = ""
    current_note_path: str = ""
    avoid_today: list[str] = field(default_factory=list)
    history: list[dict[str, Any]] = field(default_factory=list)

    @classmethod
    def from_mapping(cls, value: Any) -> "LearnerState":
        if not isinstance(value, dict):
            raise ValueError("learner-state root must be a JSON object")

        required = (
            "current_track",
            "current_source_id",
            "focus",
            "open_loop",
            "next_artifact",
            "completion_check",
        )
        missing = [
            key
            for key in required
            if not isinstance(value.get(key), str) or not value[key].strip()
        ]
        if missing:
            raise ValueError(f"Missing learner-state fields: {', '.join(missing)}")

        current_track = value["current_track"].strip()
        if current_track not in TRACKS:
            available = ", ".join(sorted(TRACKS))
            raise ValueError(
                f"current_track must be one of: {available}; got {current_track!r}"
            )

        timebox = value.get("timebox_minutes", 10)
        if isinstance(timebox, bool) or not isinstance(timebox, int):
            raise ValueError("timebox_minutes must be an integer")
        if not 1 <= timebox <= 60:
            raise ValueError("timebox_minutes must be between 1 and 60")

        avoid_today = value.get("avoid_today", [])
        if not isinstance(avoid_today, list) or not all(
            isinstance(item, str) for item in avoid_today
        ):
            raise ValueError("avoid_today must be a list of strings")

        history = value.get("history", [])
        if not isinstance(history, list) or not all(
            isinstance(item, dict) for item in history
        ):
            raise ValueError("history must be a list of objects")

        stuck_point = value.get("stuck_point", "")
        if not isinstance(stuck_point, str):
            raise ValueError("stuck_point must be a string")

        current_note_path = value.get("current_note_path", "")
        if not isinstance(current_note_path, str):
            raise ValueError("current_note_path must be a string")

        return cls(
            current_track=current_track,
            current_source_id=value["current_source_id"].strip(),
            focus=value["focus"].strip(),
            open_loop=value["open_loop"].strip(),
            next_artifact=value["next_artifact"].strip(),
            completion_check=value["completion_check"].strip(),
            timebox_minutes=timebox,
            stuck_point=stuck_point.strip(),
            current_note_path=current_note_path.strip(),
            avoid_today=[item.strip() for item in avoid_today],
            history=list(history),
        )

    @classmethod
    def load(cls, path: str | Path) -> "LearnerState":
        payload = json.loads(Path(path).read_text(encoding="utf-8"))
        return cls.from_mapping(payload)

    def to_mapping(self) -> dict[str, Any]:
        return asdict(self)

    def save(self, path: str | Path) -> None:
        destination = Path(path)
        temporary = destination.with_suffix(destination.suffix + ".tmp")
        temporary.write_text(
            json.dumps(self.to_mapping(), ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        temporary.replace(destination)


def example_state() -> LearnerState:
    return LearnerState(
        current_track="llm-systems",
        current_source_id="deep-dive-llms",
        focus="one mechanism you still cannot explain",
        open_loop=(
            "Name what changes inside the system, "
            "not only what the feature does."
        ),
        next_artifact="Write one mechanism → behavior → product-risk row",
        completion_check=(
            "The row names a mechanism and a behavior that could be observed."
        ),
        timebox_minutes=10,
        stuck_point="The current note describes the interface but not the mechanism.",
        current_note_path="notes/deep-dive-llms.md",
        avoid_today=["restart the whole lecture", "collect more sources"],
    )
