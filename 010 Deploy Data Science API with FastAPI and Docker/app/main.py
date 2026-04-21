# app/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from app.model import predict

app = FastAPI(
    title="Iris Classifier API",
    description="Predict Iris species from sepal/petal measurements",
    version="1.0.0"
)

class IrisFeatures(BaseModel):
    features: List[List[float]]  # batch of samples, each with 4 floats

@app.get("/")
def root():
    return {"message": "Iris Classifier API is running"}

@app.post("/predict/")
def get_predictions(data: IrisFeatures):
    try:
        predictions = predict(data.features)
        return {"predictions": predictions}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))