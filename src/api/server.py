from fastapi import FastAPI
from pydantic import BaseModel
from src.agents.researcher_agent import ResearcherAgent
from src.agents.writer_agent import WriterAgent

app = FastAPI(
    title="Autonomous Research Agent API",
    version="1.0.0"
)

researcher = ResearcherAgent()
writer = WriterAgent()

class ResearchRequest(BaseModel):
    topic: str

class ResearchResponse(BaseModel):
    topic: str
    report: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/research", response_model=ResearchResponse)
def research(request: ResearchRequest):
    topic = request.topic.strip()
    if not topic:
        return {"topic": "", "report": "Empty topic."}
    notes = researcher.run(topic)
    report = writer.run(notes)
    return {"topic": topic, "report": report}
