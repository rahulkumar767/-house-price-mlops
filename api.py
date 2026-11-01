
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Create FastAPI application
app = FastAPI(title="House Price Prediction API")

# Load trained model
model = joblib.load("models/house_model.joblib")

# Input data format
class HouseDetails(BaseModel):
    area_sqft: int
    bedrooms: int
    bathrooms: int
    house_age: int

# Home route
@app.get("/")
def home():
    return {"message": "House Price Prediction API is running!"}

# Prediction route
@app.post("/predict")
def predict_price(house: HouseDetails):

    input_data = pd.DataFrame([{
        "area_sqft": house.area_sqft,
        "bedrooms": house.bedrooms,
        "bathrooms": house.bathrooms,
        "house_age": house.house_age
    }])

    prediction = model.predict(input_data)

    return {
        "predicted_price": round(float(prediction[0]), 2)
    }
