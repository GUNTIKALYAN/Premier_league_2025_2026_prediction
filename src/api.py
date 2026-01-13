from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from src.model import train_model, predict

app = FastAPI(title="Premier League Predictor")


class MatchInput(BaseModel):
    Team: str
    Matches: int
    Points: int
    GoalDiff: int
    GoalsFor: int
    GoalsAgainst: int


@app.on_event("startup")  
def startup_event():
    try:
        train_model()
    except Exception as e:
        raise RuntimeError(f"Model training failed: {e}")


@app.get("/")
def welcome():
    return {"message": "Welcome to Premier League Predictor"}


@app.post("/predict")
def predict_match(data: MatchInput):
    try:
        result = predict(data.model_dump())
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
