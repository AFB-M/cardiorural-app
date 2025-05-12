import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load trained model
model = joblib.load("App/cr_model.pkl")

st.set_page_config(page_title="CardioRural: Heart Health Risk Screener", layout="centered")

st.title("CardioRural: Heart Health Risk Screener")
st.markdown(
    """
    This tool provides an **early-stage screening** for heart disease risk based on basic health information.
    It's not a diagnostic tool. Please consult a medical professional for proper evaluation.
    """
)

st.header("Patient Information")

# User inputs
age = st.number_input("Age", min_value=1, max_value=120, help="Enter your age in years")
sex = st.selectbox("Sex", options=["M", "F"], help="M: Male, F: Female")

chest_pain = st.selectbox(
    "Chest Pain Type",
    options=["TA", "ATA", "NAP", "ASY"],
    help="TA: Typical Angina, ATA: Atypical Angina, NAP: Non-Anginal Pain, ASY: Asymptomatic"
)

resting_bp = st.number_input("Resting Blood Pressure (mm Hg)", help="Typical range: 90 - 140 mm Hg")
cholesterol = st.number_input("Serum Cholesterol (mg/dl)", help="Typical range: 125 - 300 mg/dl")

fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dl?", options=[0, 1], help="1 if blood sugar > 120 mg/dl, else 0")

resting_ecg = st.selectbox(
    "Resting ECG Result",
    options=["Normal", "ST", "LVH"],
    help="Normal: Normal ECG, ST: ST-T abnormality, LVH: Left Ventricular Hypertrophy"
)

max_hr = st.number_input("Maximum Heart Rate Achieved", help="Normal range: 60 - 202 bpm")
exercise_angina = st.selectbox("Exercise-Induced Angina?", options=["Y", "N"], help="Y: Yes, N: No")

oldpeak = st.number_input("Oldpeak", help="ST depression induced by exercise (e.g., 1.4)")

st_slope = st.selectbox(
    "Slope of Peak Exercise ST Segment",
    options=["Up", "Flat", "Down"],
    help="Up: upsloping, Flat: flat, Down: downsloping"
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

# Predict and display result
if st.button("Check Risk"):
    prediction = model.predict(input_df)[0]
    risk_label = "High Risk" if prediction == 1 else "Low Risk"
    st.subheader(f"Your Risk Level: {risk_label}")
    st.info("This is an early-stage risk estimation based on basic factors.")

    st.caption("Note: This tool is for educational and preliminary screening purposes only.")
