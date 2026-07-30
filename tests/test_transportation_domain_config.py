from pathlib import Path

import yaml

from src.subscription_plan import build_pipeline_inputs


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_PROFILE_TAGS = {
    "freight-log",
    "its-control",
    "safe-infra",
    "traffic-flow",
    "trans-plan",
    "transit-rail",
}


def test_transportation_profiles_feed_both_retrieval_lanes() -> None:
    # Given: the fork's checked-in transportation engineering configuration.
    config = yaml.safe_load((ROOT / "config.yaml").read_text(encoding="utf-8"))

    # When: the production subscription planner builds its retrieval inputs.
    plan = build_pipeline_inputs(config)

    # Then: every transportation subfield reaches BM25 and semantic retrieval via arXiv.
    profile_tags = {
        profile["tag"]
        for profile in plan["profiles"]
        if profile.get("enabled", True)
    }
    assert profile_tags == EXPECTED_PROFILE_TAGS

    for lane_name in ("bm25_queries", "embedding_queries"):
        lane_queries = plan[lane_name]
        assert lane_queries
        lane_tags = {
            query["paper_tag"].split(":", maxsplit=1)[1]
            for query in lane_queries
        }
        assert EXPECTED_PROFILE_TAGS <= lane_tags
        assert all(query["paper_sources"] == ["arxiv"] for query in lane_queries)
