import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load model safely
try:
    with open("model.pkl", "rb") as file:
        model = pickle.load(file)
except:
    st.error("❌ Model file not found. Please upload model.pkl")
    st.stop()

# Title
st.title("💳 Digital Payment Impact Model")
st.subheader("Analyzing UPI Growth Impact on Bank Profitability")

# Description
st.write("""
This model predicts **Bank Profit** based on **Digital Payment (UPI) Volume**.
It demonstrates how increasing digital transactions can influence financial performance.
""")

# Sidebar input
st.sidebar.header("User Input")

upi_value = st.sidebar.number_input(
    "Enter UPI Transaction Value (in Crores ₹)",
    min_value=0.0,
    value=1000.0
)

# Prediction
if st.button("Predict Profit"):
    try:
        input_data = np.array([[upi_value]])
        prediction = model.predict(input_data)

        st.success(f"💰 Estimated Profit: ₹ {prediction[0]:,.2f} Crores")

    except:
        st.error("⚠️ Prediction error. Check model.")

# Optional Visualization
st.subheader("📊 Sample Data Visualization")

# Dummy sample data (for presentation)
data = pd.DataFrame({
    "UPI_Value": [500, 1000, 1500, 2000, 2500],
    "Profit": [25, 50, 75, 100, 125]
})

st.line_chart(data)

# Footer
st.markdown("---")
st.caption("Developed for ABA Project | Digital Payments Analysis")
