from ai_tutor_bot.progress import record_progress
from ai_tutor_bot.state import LearnerState


def test_record_progress_preserves_a_small_history():
    state = LearnerState.load("examples/learner-state.json")
    old_loop = state.open_loop

    record_progress(
        state,
        artifact="notes/tool-use.md",
        reflection="The revised sentence now names the external check.",
        next_open_loop="Separate tool selection from tool-result verification.",
        next_artifact="Add one failure row to notes/tool-use.md",
        next_check="The row distinguishes selection failure from result-check failure.",
    )

    assert state.history[-1]["completed_open_loop"] == old_loop
    assert state.history[-1]["artifact"] == "notes/tool-use.md"
    assert state.open_loop.startswith("Separate tool selection")
    assert state.completion_check.startswith("The row distinguishes")
