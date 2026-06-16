
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np


app = FastAPI()

model = joblib.load("pumpkin_seeds.pkl")

class PumpkinData(BaseModel):

    Area: float
    Perimeter: float
    Major_Axis_Length: float
    Minor_Axis_Length: float
    Convex_Area: float
    Equiv_Diameter: float
    Solidity: float
    Roundness: float
    Compactness: float
    Shape_Factor_1: float

@app.get("/")
def home():

    return {
        "message":"Pumpkin Seed Classifier API"
    }

@app.post("/predict")
def predict(data: PumpkinData):

    features=np.array([
        [
            data.Area,
            data.Perimeter,
            data.Major_Axis_Length,
            data.Minor_Axis_Length,
            data.Convex_Area,
            data.Equiv_Diameter,
            data.Solidity,
            data.Roundness,
            data.Compactness,
            data.Shape_Factor_1
        ]
    ])

    prediction=model.predict(features)

    label = (
        "CERCEVELIK"
        if prediction[0]==0
        else "URGUP_SIVRISI"
    )

    return {
        "prediction":label
    }