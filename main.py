from fastapi import FastAPI
from pydantic import BaseModel
from recommendation import get_recommendations

app = FastAPI()

class QueryInput(BaseModel):
    query: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/recommend")
def recommend(input: QueryInput):
    recommendations = get_recommendations(input.query)
    return {"results": recommendations}