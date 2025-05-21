
import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("App/cr_model.pkl")

st.set_page_config(page_title="CardioRural: Heart Health Risk Screener", layout="centered")

st.title("CardioRural: Heart Health Risk Checker")

st.markdown(
    """
    This tool provides an **early-stage screening** for heart disease risk based on basic health information.
    It's not a diagnostic tool. Please consult a medical professional for proper evaluation.
    """
)

st.header("Patient Information")

# Validation function
def validated_float_input(label, min_val, max_val, help_text=""):
    val = st.text_input(label, help=help_text)
    try:
        float_val = float(val)
        if float_val < min_val or float_val > max_val:
            st.warning(f"{label} should be between {min_val} and {max_val}.")
            return None
        return float_val
    except:
        if val != "":
            st.warning(f"Please enter a valid number for {label}.")
        return None

# Inputs
age = validated_float_input("Age", 0, 120, "Enter age in years")
sex = st.selectbox("Sex", options=["M", "F"], help="M: Male, F: Female")
chest_pain = st.selectbox("Chest Pain Type", options=["TA", "ATA", "NAP", "ASY"])
resting_bp = validated_float_input("Resting Blood Pressure (mm Hg)", 60, 200, "e.g., 120")
cholesterol = validated_float_input("Serum Cholesterol (mg/dl)", 100, 600, "e.g., 200")
fasting_bs = validated_float_input("Fasting Blood Sugar (mg/dl)", 50, 400, "Enter measured glucose level")
resting_ecg = st.selectbox("Resting ECG Result", options=["Normal", "ST", "LVH"])
max_hr = validated_float_input("Maximum Heart Rate Achieved", 40, 220, "e.g., 150")
exercise_angina = st.selectbox("Exercise-Induced Angina?", options=["Y", "N"])
oldpeak = validated_float_input("Oldpeak", 0.0, 6.0, "ST depression induced by exercise (e.g., 1.4)")
st_slope = st.selectbox("Slope of Peak Exercise ST Segment", options=["Up", "Flat", "Down"])

# Only proceed if all inputs are valid
if st.button("Check Risk"):
    input_values = [age, resting_bp, cholesterol, fasting_bs, max_hr, oldpeak]
    if any(v is None for v in input_values):
        st.error("Please enter all numeric values correctly before checking risk.")
    else:
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
        prediction = model.predict(input_df)[0]
        risk_label = "High Risk" if prediction == 1 else "Low Risk"
        st.subheader(f"Your Risk Level: {risk_label}")
        st.info("This is an early-stage risk estimation based on basic factors.")
        st.caption("Note: This tool is for educational and preliminary screening purposes only.")
