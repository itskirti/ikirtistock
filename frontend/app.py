import streamlit as st
import requests

st.title("📈 Stock Market Prediction")

# User input
st.write("Enter stock data for prediction:")
user_input = st.text_area("Stock Data (comma-separated):")

if st.button("Predict"):
    try:
        data = [float(i) for i in user_input.split(",")]
        response = requests.post("http://127.0.0.1:8000/predict", json={"data": data})
        prediction = response.json().get("prediction", "Error in prediction")
        st.write("### Predicted Stock Price:", prediction)
    except:
        st.error("Invalid input. Please enter numerical values separated by commas.")
