import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load trained model
model = joblib.load("App/cr_model.pkl")

st.set_page_config(page_title="CardioRural: Heart Health Risk Screener", layout="centered")

st.title("CardioRural: Heart Health Risk Checker")

st.markdown(
    """
    This tool is intended for **informational use by healthcare professionals**.  
    It provides an early-stage screening of heart disease risk based on basic clinical data.  
    It is **not** a diagnostic tool.
    """
)

st.header("Patient Information")

# User inputs
age = st.number_input("Age", min_value=1, max_value=120, help="Enter age in years")
sex = st.selectbox("Sex", options=["M", "F"], help="M: Male, F: Female")

chest_pain = st.selectbox(
    "Chest Pain Type",
    options=["TA", "ATA", "NAP", "ASY"],
    help="TA: Typical Angina, ATA: Atypical Angina, NAP: Non-Anginal Pain, ASY: Asymptomatic"
)

resting_bp = st.number_input("Resting Blood Pressure (mm Hg)", help="e.g., 120")
cholesterol = st.number_input("Serum Cholesterol (mg/dl)", help="e.g., 200")

fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dl?", options=[0, 1], help="1 = Yes, 0 = No")

resting_ecg = st.selectbox(
    "Resting ECG Result",
    options=["Normal", "ST", "LVH"]
)

max_hr = st.number_input("Maximum Heart Rate Achieved", help="e.g., 150")
exercise_angina = st.selectbox("Exercise-Induced Angina?", options=["Y", "N"], help="Y = Yes, N = No")

oldpeak = st.number_input("Oldpeak", help="ST depression induced by exercise (e.g., 1.4)")

st_slope = st.selectbox(
    "Slope of Peak Exercise ST Segment",
    options=["Up", "Flat", "Down"]
)

# Convert inputs to DataFrame
input_dict = {
    "Age": [age],
    "Sex": [sex],
    "ChestPainType": [chest_pain],
    "RestingBP": [resting_bp],
    "Cholesterol": [cholesterol],
    "FastingBS": [fasting_bs],
    "RestingECG": [resting_ecg],
    "MaxHR": [max_hr],
    "ExerciseAngina": [exercise_angina],
    "Oldpeak": [oldpeak],
    "ST_Slope": [st_slope]
}

input_df = pd.DataFrame(input_dict)

if st.button("Check Risk"):
    prediction = model.predict(input_df)[0]
    risk_label = "High Risk" if prediction == 1 else "Low Risk"
    st.subheader(f"Predicted Risk Level: {risk_label}")
    st.caption("This is an early-stage estimation tool and should not replace clinical judgment.")
