from __future__ import annotations

from datetime import datetime, timezone

from .state import LearnerState


def record_progress(
    state: LearnerState,
    *,
    artifact: str,
    reflection: str,
    next_open_loop: str,
    next_artifact: str,
    next_check: str,
) -> LearnerState:
    if not artifact.strip():
        raise ValueError("artifact cannot be empty")
    next_values = (next_open_loop, next_artifact, next_check)
    if not all(value.strip() for value in next_values):
        raise ValueError("the next open loop, artifact, and check cannot be empty")

    state.history.append(
        {
            "recorded_at": datetime.now(timezone.utc).isoformat(),
            "artifact": artifact.strip(),
            "reflection": reflection.strip(),
            "completed_open_loop": state.open_loop,
        }
    )
    state.open_loop = next_open_loop.strip()
    state.next_artifact = next_artifact.strip()
    state.completion_check = next_check.strip()
    return state
