import pytest

from karpathy_course_tutor.state import LearnerState


def valid_state() -> dict:
    return {
        "current_track": "llm-systems",
        "current_source_id": "deep-dive-llms",
        "focus": "tool use",
        "open_loop": "Explain what the model checked.",
        "next_artifact": "Rewrite one sentence.",
        "completion_check": "The sentence names returned evidence.",
        "timebox_minutes": 10,
        "avoid_today": ["restart the lecture"],
        "history": [],
    }


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("avoid_today", "restart", "list of strings"),
        ("history", {"artifact": "notes.md"}, "list of objects"),
        ("timebox_minutes", True, "must be an integer"),
        ("current_track", "unknown", "must be one of"),
    ],
)
def test_rejects_invalid_field_shapes(field, value, message):
    payload = valid_state()
    payload[field] = value

    with pytest.raises(ValueError, match=message):
        LearnerState.from_mapping(payload)


def test_rejects_non_object_root():
    with pytest.raises(ValueError, match="root must be a JSON object"):
        LearnerState.from_mapping([])
