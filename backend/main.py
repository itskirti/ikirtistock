from fastapi import FastAPI
import tensorflow as tf
import numpy as np
from pydantic import BaseModel
from typing import List
import os

app = FastAPI()

# Load your trained LSTM model
model_path = os.path.join(os.path.dirname(os.getcwd()), "model/lstm_stock_model.h5")
model = tf.keras.models.load_model(model_path)

class StockInput(BaseModel):
    data: List[float]  # Ensuring a list of floats

@app.post("/predict")
def predict_stock(input_data: StockInput):
    # Convert input to NumPy array and reshape for LSTM model
    input_array = np.array(input_data.data, dtype=np.float32).reshape(1, -1, 1)
    prediction = model.predict(input_array)
    return {"prediction": prediction.tolist()}


