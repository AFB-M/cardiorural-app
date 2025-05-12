import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load model
model = joblib.load("cr_model.pkl")  # make sure it's in the same directory or use full path

# Function to preprocess input
def preprocess_input(age, sex, chest_pain, resting_bp, cholesterol, fasting_bs, ecg, max_hr, angina, oldpeak, slope):
    # Encode categorical values as done in training
    sex = 1 if sex == "M" else 0
    chest_pain_map = {"TA": 0, "ATA": 1, "NAP": 2, "ASY": 3}
    ecg_map = {"Normal": 0, "ST": 1, "LVH": 2}
    angina = 1 if angina == "Y" else 0
    slope_map = {"Up": 0, "Flat": 1, "Down": 2}

    # Construct input vector
    input_data = np.array([
        age, sex, chest_pain_map[chest_pain], resting_bp, cholesterol, fasting_bs,
        ecg_map[ecg], max_hr, angina, oldpeak, slope_map[slope]
    ]).reshape(1, -1)

    return input_data

# UI
st.title("CardioRural: Heart Health Risk Screener")
st.header("Enter Your Information")

age = st.number_input("Age (years)", help="Age of the patient in years")
sex = st.selectbox("Sex", options=["M", "F"], help="Male or Female")
chest_pain = st.selectbox(
    "Chest Pain Type",
    options=["TA", "ATA", "NAP", "ASY"],
    help="TA: Typical Angina, ATA: Atypical Angina, NAP: Non-Anginal Pain, ASY: Asymptomatic"
)
resting_bp = st.number_input("Resting Blood Pressure (mm Hg)", help="Patient's resting blood pressure")
cholesterol = st.number_input("Serum Cholesterol (mg/dl)", help="Patient's serum cholesterol level")
fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dl?", options=[0, 1], help="1 if fasting blood sugar > 120 mg/dl, else 0")
resting_ecg = st.selectbox(
    "Resting ECG Result",
    options=["Normal", "ST", "LVH"],
    help="Normal, ST: ST-T wave abnormality, LVH: Left Ventricular Hypertrophy"
)
max_hr = st.number_input("Maximum Heart Rate Achieved", help="Measured during exercise test")
exercise_angina = st.selectbox("Exercise-Induced Angina?", options=["Y", "N"], help="Y: Yes, N: No")
oldpeak = st.number_input("Oldpeak", help="ST depression induced by exercise")
st_slope = st.selectbox(
    "Slope of Peak Exercise ST Segment",
    options=["Up", "Flat", "Down"],
    help="Up: upsloping, Flat: flat, Down: downsloping"
)

# Prediction
if st.button("Check Risk"):
    user_input = preprocess_input(age, sex, chest_pain, resting_bp, cholesterol, fasting_bs, ecg, max_hr, angina, oldpeak, slope)
    prediction = model.predict(user_input)[0]
    prob = model.predict_proba(user_input)[0][1] * 100

    if prediction == 1:
        st.error(f"High Risk Detected: {prob:.2f}% probability of heart disease.")
    else:
        st.success(f"Low Risk: {100 - prob:.2f}% probability of being healthy.")

    st.caption("This is an AI-based early prediction and does not replace professional medical diagnosis.")
