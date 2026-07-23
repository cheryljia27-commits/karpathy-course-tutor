from pathlib import Path

from karpathy_course_tutor.catalog import find_source, load_course_map


def test_course_map_is_unique_and_primary_linked():
    sources = load_course_map()
    ids = [source.id for source in sources]

    assert len(sources) >= 12
    assert len(ids) == len(set(ids))
    assert all(source.url.startswith("https://") for source in sources)
    assert {source.track for source in sources} == {
        "llm-systems",
        "agent-loops",
        "evaluation",
    }


def test_find_source_has_actionable_metadata():
    source = find_source("deep-dive-llms", load_course_map())

    assert source.priority == 0
    assert "mechanism" in source.teaching_move.lower()
    assert "artifact" not in source.minimum_artifact.lower()


def test_public_source_maps_cover_every_runtime_source():
    source_pack = Path(
        "source-packs/karpathy-ai-systems/course-map.md"
    ).read_text(encoding="utf-8")
    skill_reference = Path(
        "skill/karpathy-course-tutor/references/course-map.md"
    ).read_text(encoding="utf-8")

    for source in load_course_map():
        assert source.url in source_pack, source.id
        assert source.url in skill_reference, source.id
