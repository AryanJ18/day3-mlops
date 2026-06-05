from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

model = joblib.load("model.pkl")

class FlowerData(BaseModel):
    sepal_lenght: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.get("/")
def home():
    return {"message": "Welcometo to the FastAPI application"}

@app.post("/predict")
def predict(data: FlowerData):
    prediction = model.predict([[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
     ]])
    return {"Prediction": int(prediction[0])}
 