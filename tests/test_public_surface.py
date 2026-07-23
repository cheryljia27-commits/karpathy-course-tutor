from pathlib import Path


def test_public_identity_is_ai_tutor_bot():
    readme = Path("README.md").read_text(encoding="utf-8")
    metadata = Path("pyproject.toml").read_text(encoding="utf-8")
    normalized_readme = " ".join(readme.split())

    assert readme.startswith("# AI Tutor Bot\n")
    assert 'name = "ai-tutor-bot"' in metadata
    assert "continuation layer for learning" in normalized_readme
    assert "Karpathy Course Tutor" not in readme + metadata


def test_sanitized_loop_matches_the_recorded_reentry():
    loop = Path("examples/sanitized-tutor-loop.md").read_text(encoding="utf-8")

    assert "No need to rebuild the plan this morning." in loop
    assert "Your note already points back to tool use and web search." in loop
    assert "Make the sentence say what the model checked" in loop
