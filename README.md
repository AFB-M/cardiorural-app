# CardioRural

**Preventing cardiovascular disease in rural African communities using data-driven mobile screening tools.**

CardioRural is an open-source, mobile-friendly cardiovascular risk assessment tool built with [Streamlit](https://streamlit.io/). It’s designed to support underserved rural populations by enabling preventive heart screening through accessible technology.

![CardioRural Screenshot](https://github.com/AFB-M/cardiorural-app/blob/main/CardioRural.PNG)

---

## 🚀 Try the App

👉 [Launch CardioRural Now](https://cardiopre-app-aw.streamlit.app/)

---

## 💡 Why CardioRural?

Cardiovascular disease (CVD) remains a top cause of death in Nigeria, with rural communities disproportionately affected due to limited access to early screening tools.

CardioRural bridges this gap by:
- Using simple clinical inputs to estimate risk
- Delivering personalized lifestyle tips
- Running on mobile devices with offline potential

---

## 🔧 Key Features

- Intuitive, mobile-first user interface
- Collects core health metrics: age, sex, blood pressure, chest pain, blood sugar, etc.
- Predicts heart disease risk (Low, Moderate, High)
- Provides health guidance based on risk score

---

## 🧪 How It Works

This version uses a **trained machine learning model (Logistic Regression)** to estimate heart disease risk. Built using:
- Publicly available datasets (e.g., [Kaggle Heart Disease Dataset](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction))
- Preprocessing pipeline with `ColumnTransformer`
- Scikit-learn model serialized via `joblib`

Planned upgrades:
- Tailored models for African populations
- Real-world community data integration

---

## ⚙️ Tech Stack

- Python 🐍  
- Streamlit 📱  
- Pandas 📊  
- Scikit-learn 🤖

---

## 🛤️ Roadmap

- ✅ MVP app live and functional  
- 🔲 Local language support (Yoruba, Hausa, Igbo)  
- 🔲 SMS-based access  
- 🔲 AI-powered smart triage  
- 🔲 Collaboration with NGOs & PHCs for real-world deployment

---

## 📜 License

This project is licensed under the **MIT License** – open for use, improvement, and deployment.

---

## 👤 Author

**Afolabi Mahmood Olalekan**  
Medical Student • Data Scientist • Digital Health Advocate  
🌍 Nigeria  
🔗 [LinkedIn](https://www.linkedin.com/in/afolabi-mahmood-olalekan/) | 🔗 [GitHub](https://github.com/AFB-M)

---

> ⚠️ **Disclaimer:** This tool is for educational and preliminary screening purposes only. It is not a substitute for professional medical diagnosis or treatment.
