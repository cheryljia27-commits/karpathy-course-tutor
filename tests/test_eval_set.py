import json
from pathlib import Path

from karpathy_course_tutor.catalog import find_source, load_course_map
from karpathy_course_tutor.engine import evaluate_message
from karpathy_course_tutor.state import LearnerState


def test_public_eval_set_matches_expected_labels():
    cases = json.loads(
        Path("examples/eval-set.json").read_text(encoding="utf-8")
    )
    sources = load_course_map()

    for case in cases:
        state = LearnerState.load(case["learner_state"])
        source = find_source(state.current_source_id, sources)
        result = evaluate_message(case["message"], state, source)
        assert result.label == case["expected_label"], case["name"]
