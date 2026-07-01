# app/main.py
from fastapi import FastAPI
from .schemas import SensorData, PredictionResponse
from .model_logic import get_prediction

app = FastAPI(title="Mission Analytics API")

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/predict", response_model=PredictionResponse)
def predict(data: SensorData):
    # The 'data' object here is already validated by Pydantic
    prob = get_prediction(data.model_dump())
    return {
        "status": "success",
        "failure_probability": prob
    }