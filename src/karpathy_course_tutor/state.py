from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any


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
    avoid_today: list[str] = field(default_factory=list)
    history: list[dict[str, Any]] = field(default_factory=list)

    @classmethod
    def from_mapping(cls, value: dict[str, Any]) -> "LearnerState":
        required = (
            "current_track",
            "current_source_id",
            "focus",
            "open_loop",
            "next_artifact",
            "completion_check",
        )
        missing = [key for key in required if not str(value.get(key, "")).strip()]
        if missing:
            raise ValueError(f"Missing learner-state fields: {', '.join(missing)}")

        timebox = int(value.get("timebox_minutes", 10))
        if not 1 <= timebox <= 60:
            raise ValueError("timebox_minutes must be between 1 and 60")

        return cls(
            current_track=str(value["current_track"]).strip(),
            current_source_id=str(value["current_source_id"]).strip(),
            focus=str(value["focus"]).strip(),
            open_loop=str(value["open_loop"]).strip(),
            next_artifact=str(value["next_artifact"]).strip(),
            completion_check=str(value["completion_check"]).strip(),
            timebox_minutes=timebox,
            stuck_point=str(value.get("stuck_point", "")).strip(),
            avoid_today=[str(item) for item in value.get("avoid_today", [])],
            history=list(value.get("history", [])),
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
        avoid_today=["restart the whole lecture", "collect more sources"],
    )
