import pickle
import os

MODEL_PATH = os.getenv("MODEL_PATH", "models/model.pkl")

def load_model():
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    return model 

model = load_model()

def predict(features: list):
    return model.predict(features).tolist()
