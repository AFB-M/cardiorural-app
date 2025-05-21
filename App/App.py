import streamlit as st
import pandas as pd
import joblib

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

# Input functions for clean number entry
def safe_float_input(label, help_text=""):
    val = st.text_input(label, help=help_text)
    try:
        return float(val)
    except:
        return None

# Inputs
age = safe_float_input("Age", "Enter age in years")
sex = st.selectbox("Sex", options=["M", "F"], help="M: Male, F: Female")

chest_pain = st.selectbox(
    "Chest Pain Type",
    options=["TA", "ATA", "NAP", "ASY"],
    help="TA: Typical Angina, ATA: Atypical Angina, NAP: Non-Anginal Pain, ASY: Asymptomatic"
)

resting_bp = safe_float_input("Resting Blood Pressure (mm Hg)", "e.g., 120")
cholesterol = safe_float_input("Serum Cholesterol (mg/dl)", "e.g., 200")

#
fasting_bs = safe_float_input("Fasting Blood Sugar (mg/dl)", "Enter measured blood glucose level in mg/dl")

resting_ecg = st.selectbox("Resting ECG Result", options=["Normal", "ST", "LVH"])

max_hr = safe_float_input("Maximum Heart Rate Achieved", "e.g., 150")
exercise_angina = st.selectbox("Exercise-Induced Angina?", options=["Y", "N"], help="Y = Yes, N = No")

oldpeak = safe_float_input("Oldpeak", "ST depression induced by exercise (e.g., 1.4)")
st_slope = st.selectbox("Slope of Peak Exercise ST Segment", options=["Up", "Flat", "Down"])

# Validation and model input
if st.button("Check Risk"):
    inputs = [age, sex, chest_pain, resting_bp, cholesterol, fasting_bs,
              resting_ecg, max_hr, exercise_angina, oldpeak, st_slope]

    if None in inputs:
        st.warning("Please enter valid numeric values for all fields.")
    else:
        input_dict = {
            "Age": [age],
            "Sex": [sex],
            "ChestPainType": [chest_pain],
            "RestingBP": [resting_bp],
            "Cholesterol": [cholesterol],
            "FastingBS": [1 if fasting_bs > 120 else 0],  # binarize as expected by model
            "RestingECG": [resting_ecg],
            "MaxHR": [max_hr],
            "ExerciseAngina": [exercise_angina],
            "Oldpeak": [oldpeak],
            "ST_Slope": [st_slope]
        }

        input_df = pd.DataFrame(input_dict)
        prediction = model.predict(input_df)[0]
        risk_label = "High Risk" if prediction == 1 else "Low Risk"

        st.subheader(f"Predicted Risk Level: {risk_label}")
        st.caption("This is an early-stage estimation tool and should not replace clinical judgment.")
