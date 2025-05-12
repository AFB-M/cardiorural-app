import streamlit as st

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

    st.subheader(f"Your Risk Level: {risk_label}")
    st.info("This is an early-stage risk estimation based on basic factors.")
