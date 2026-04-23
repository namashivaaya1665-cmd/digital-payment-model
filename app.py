import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("Digital Payment Impact Model")

st.write("Predict Profit based on UPI Transaction Value")

upi_value = st.number_input("Enter UPI Transaction Value", min_value=0.0)

if st.button("Predict"):
    prediction = model.predict([[upi_value]])
    st.success(f"Estimated Profit: {prediction[0]:.2f}")
