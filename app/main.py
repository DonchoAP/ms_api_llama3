from fastapi import FastAPI, HTTPException
from .database import engine
from . import models
from .api import general_info, symptoms, statistics, treatments, research_advances
from .llama import llama

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Multiple Sclerosis Research API",
    description="This API provides access to up-to-date and relevant information on Multiple Sclerosis (MS), covering data from the year 2000 to the present.",
    version="1.0.0",
)

app.include_router(general_info.router, tags=["General Info"])
app.include_router(symptoms.router, tags=["Symptoms"])
app.include_router(statistics.router, tags=["Statistics"])
app.include_router(treatments.router, tags=["Treatments"])
app.include_router(research_advances.router, tags=["Research Advances"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Multiple Sclerosis Research API"}

@app.get("/ask-llama/{question}")
async def ask_llama(question: str):
    try:
        prompt = f"Question about Multiple Sclerosis: {question}\nAnswer:"
        response = llama.generate_response(prompt)
        return {"question": question, "answer": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))