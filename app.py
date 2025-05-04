import streamlit as st

st.title("CardioRural: Heart Health Risk Screener")

st.header("Enter Your Information")
age = st.slider("Age", 18, 100)
gender = st.selectbox("Gender", ["Male", "Female"])
weight = st.number_input("Weight (kg)")
bp = st.selectbox("Do you have high blood pressure?", ["Yes", "No"])
smoke = st.selectbox("Do you smoke?", ["Yes", "No"])
diabetes = st.selectbox("Do you have diabetes?", ["Yes", "No"])

if st.button("Check Risk"):
    # Placeholder logic
    risk_score = 0
    if bp == "Yes": risk_score += 1
    if smoke == "Yes": risk_score += 1
    if diabetes == "Yes": risk_score += 1
    risk_label = ["Low", "Moderate", "High"][min(risk_score, 2)]

    st.subheader(f"Your Risk Level: {risk_label}")
    st.info("This is an early-stage risk estimation based on basic factors.")
