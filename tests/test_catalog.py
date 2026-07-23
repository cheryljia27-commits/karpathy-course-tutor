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
