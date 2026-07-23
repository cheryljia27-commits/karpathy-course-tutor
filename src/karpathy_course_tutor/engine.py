from __future__ import annotations

from dataclasses import dataclass

from .catalog import CourseSource
from .state import LearnerState


@dataclass(frozen=True, slots=True)
class EvalResult:
    label: str
    failures: tuple[str, ...]
    checks: dict[str, bool]


def _sentence(value: str) -> str:
    value = value.strip()
    if not value:
        return value
    return value if value[-1] in ".!?" else value + "."


def build_reentry_message(state: LearnerState, source: CourseSource) -> str:
    return (
        f"Don't restart the whole course. Return to “{state.focus}”: "
        f"{_sentence(state.open_loop)} "
        f"Spend {state.timebox_minutes} minutes on one artifact: "
        f"{_sentence(state.next_artifact)} "
        f"Check: {_sentence(state.completion_check)} "
        f"Source: {source.title} → {source.url}"
    )


def evaluate_message(
    message: str,
    state: LearnerState,
    source: CourseSource,
) -> EvalResult:
    normalized = message.casefold()
    artifact_anchor = state.next_artifact.casefold()[:28]
    check_anchor = state.completion_check.casefold()[:28]
    open_loop_anchor = state.open_loop.casefold()[:28]
    persona_phrases = (
        "karpathy would say",
        "as karpathy",
        "i am andrej",
        "pretend to be karpathy",
        "in karpathy's voice",
    )

    checks = {
        "right_reentry": (
            state.focus.casefold() in normalized or open_loop_anchor in normalized
        ),
        "has_artifact": artifact_anchor in normalized,
        "has_completion_check": check_anchor in normalized,
        "has_timebox": str(state.timebox_minutes) in message,
        "has_primary_source": source.url in message,
        "low_bandwidth": len(message) <= 650,
        "no_persona_simulation": not any(
            phrase in normalized for phrase in persona_phrases
        ),
    }

    failure_names = {
        "right_reentry": "wrong-re-entry",
        "has_artifact": "no-artifact",
        "has_completion_check": "no-verification",
        "has_timebox": "missing-timebox",
        "has_primary_source": "missing-source",
        "low_bandwidth": "too-heavy",
        "no_persona_simulation": "persona-risk",
    }
    failures = tuple(
        failure_names[name] for name, passed in checks.items() if not passed
    )

    if not failures:
        label = "pass"
    elif set(failures) <= {"missing-timebox", "too-heavy"}:
        label = "soft-pass"
    else:
        label = "fail"

    return EvalResult(label=label, failures=failures, checks=checks)
