import streamlit as st
import numpy as np

# Title & description
st.title("🩺 Diabetes Prediction App")
st.write("Fill in the details below and click **Predict** to see the result.")

# Input fields
age = st.number_input("Age", min_value=1, max_value=120, value=25)
glucose = st.number_input("Glucose Level", min_value=0, max_value=300, value=100)
blood_pressure = st.number_input("Blood Pressure", min_value=0, max_value=200, value=70)
bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=22.5)

# Prediction button
if st.button("Predict"):
    # ---------- MOCK MODEL (replace with your ML model later) ----------
    # Simple rule: If glucose > 125 or BMI > 30 → higher risk
    if glucose > 125 or bmi > 30:
        prediction = 1  # Diabetic
    else:
        prediction = 0  # Not Diabetic
    # ------------------------------------------------------------------

    # Show result
    if prediction == 1:
        st.error("⚠️ The model predicts: **Diabetic**")
    else:
        st.success("✅ The model predicts: **Not Diabetic**")

    # Debug (optional)
    st.info(f"(Debug Info: Age={age}, Glucose={glucose}, BP={blood_pressure}, BMI={bmi})")
