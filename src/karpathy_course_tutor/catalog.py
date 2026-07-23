from __future__ import annotations

import json
from dataclasses import dataclass
from importlib.resources import files
from typing import Any


@dataclass(frozen=True, slots=True)
class CourseSource:
    id: str
    title: str
    url: str
    kind: str
    track: str
    priority: int
    teaching_move: str
    minimum_artifact: str

    @classmethod
    def from_mapping(cls, value: dict[str, Any]) -> "CourseSource":
        return cls(
            id=str(value["id"]),
            title=str(value["title"]),
            url=str(value["url"]),
            kind=str(value["kind"]),
            track=str(value["track"]),
            priority=int(value["priority"]),
            teaching_move=str(value["teaching_move"]),
            minimum_artifact=str(value["minimum_artifact"]),
        )


def load_course_map() -> list[CourseSource]:
    path = files("karpathy_course_tutor").joinpath("data/course_map.json")
    payload = json.loads(path.read_text(encoding="utf-8"))
    return [CourseSource.from_mapping(item) for item in payload["sources"]]


def find_source(source_id: str, sources: list[CourseSource]) -> CourseSource:
    for source in sources:
        if source.id == source_id:
            return source
    available = ", ".join(sorted(source.id for source in sources))
    raise ValueError(f"Unknown source_id {source_id!r}. Available: {available}")
