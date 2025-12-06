from src.pipelines.research_pipeline import ResearchPipeline

def test_pipeline_runs():
    p = ResearchPipeline(allow_network=False)
    out = p.run("AI Agents 2025")
    assert isinstance(out, str)
    assert len(out) > 10