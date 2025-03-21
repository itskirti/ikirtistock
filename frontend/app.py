import streamlit as st
import requests
import numpy as np

# FastAPI backend URL
BACKEND_URL = "http://127.0.0.1:8000/predict"

st.title("Stock Price Prediction")

# Input field for stock data
user_input = st.text_input("Enter stock data (comma-separated values):")

if st.button("Predict"):
    try:
        # Convert input to list of floats
        input_data = [float(x.strip()) for x in user_input.split(",")]

        # Send request to FastAPI backend
        response = requests.post(BACKEND_URL, json={"data": input_data})

        if response.status_code == 200:
            prediction = response.json().get("prediction", "Error")
            st.success(f"Predicted Stock Price: {prediction}")
        else:
            st.error("Failed to get a prediction. Check backend logs.")

    except ValueError:
        st.error("Invalid input! Enter numeric values separated by commas.")

