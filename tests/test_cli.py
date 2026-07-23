import json

import pytest

from karpathy_course_tutor.cli import main


def test_cli_reports_invalid_state_without_traceback(tmp_path, capsys):
    state_path = tmp_path / "learner-state.json"
    state_path.write_text("{not-json}\n", encoding="utf-8")

    with pytest.raises(SystemExit) as exit_info:
        main(["next", "--state", str(state_path)])

    captured = capsys.readouterr()
    assert exit_info.value.code == 2
    assert captured.out == ""
    assert "karpathy-tutor: error:" in captured.err
    assert "Traceback" not in captured.err


def test_cli_record_round_trip(tmp_path):
    state_path = tmp_path / "learner-state.json"

    assert main(["init", "--output", str(state_path)]) == 0
    assert (
        main(
            [
                "record",
                "--state",
                str(state_path),
                "--artifact",
                "notes/tool-use.md",
                "--reflection",
                "The note now names the returned evidence.",
                "--next-open-loop",
                "Distinguish selection from verification.",
                "--next-artifact",
                "Add one failure row.",
                "--next-check",
                "The row names both failure surfaces.",
            ]
        )
        == 0
    )

    payload = json.loads(state_path.read_text(encoding="utf-8"))
    assert payload["history"][-1]["artifact"] == "notes/tool-use.md"
    assert payload["open_loop"] == "Distinguish selection from verification."
