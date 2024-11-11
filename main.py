from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agents import summarize_text, question_answering, generate_future_directions
from database import GraphDB

app = FastAPI()
db = GraphDB("bolt://localhost:7687", "neo4j", "password")

class QueryRequest(BaseModel):
    topic: str
    content: str

@app.post("/summarize")
async def summarize_content(request: QueryRequest):
    summary = summarize_text(request.content)
    db.store_paper(request.topic, "Generated Summary", 2024, summary)
    return {"summary": summary}

@app.post("/ask")
async def answer_question(request: QueryRequest):
    answer = question_answering(request.content, request.topic)
    return {"answer": answer}

@app.post("/generate_directions")
async def generate_future(request: QueryRequest):
    directions = generate_future_directions(request.content)
    return {"directions": directions}

@app.get("/papers/{topic}")
async def get_papers(topic: str):
    return db.get_all_papers(topic)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
