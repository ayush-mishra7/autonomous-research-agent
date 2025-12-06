from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.pipelines.research_pipeline import ResearchPipeline

app = FastAPI(title="ARA API", version="1.0")

pipeline = ResearchPipeline(allow_network=False)

class QueryIn(BaseModel):
    query: str

@app.post("/ask")
def ask(payload: QueryIn):
    if not payload.query.strip():
        raise HTTPException(status_code=400, detail="Empty query")
    return {"report": pipeline.run(payload.query)}
