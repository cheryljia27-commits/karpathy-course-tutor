from ai_tutor_bot.catalog import find_source, load_course_map
from ai_tutor_bot.engine import build_reentry_message, evaluate_message
from ai_tutor_bot.state import LearnerState


def sample_state() -> LearnerState:
    return LearnerState.load("examples/learner-state.json")


def sample_source():
    return find_source("deep-dive-llms", load_course_map())


def test_generated_message_passes_invariants():
    state = sample_state()
    source = sample_source()
    message = build_reentry_message(state, source)
    result = evaluate_message(message, state, source)

    assert result.label == "pass"
    assert result.failures == ()
    assert state.open_loop in message
    assert state.next_artifact in message
    assert state.completion_check in message
    assert source.url in message


def test_generic_message_fails():
    result = evaluate_message(
        "Would you like to study AI today?",
        sample_state(),
        sample_source(),
    )

    assert result.label == "fail"
    assert "wrong-re-entry" in result.failures
    assert "no-artifact" in result.failures
    assert "no-verification" in result.failures
    assert "missing-source" in result.failures


def test_persona_simulation_fails():
    state = sample_state()
    source = sample_source()
    message = (
        "Karpathy would say: "
        f"{state.focus} {state.next_artifact} in {state.timebox_minutes} minutes "
        f"{state.completion_check} "
        f"{source.url}"
    )

    result = evaluate_message(message, state, source)

    assert result.label == "fail"
    assert "persona-risk" in result.failures
