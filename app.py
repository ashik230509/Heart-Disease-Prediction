import joblib

model = joblib.load("heart_model.pkl")
import streamlit as st

st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️"
)
st.sidebar.title("About")

st.sidebar.info(
    """
    This application predicts the likelihood of heart disease
    using a Logistic Regression model trained with Scikit-learn.

    Developed by Ashik
    """
)

st.title("❤️ Heart Disease Prediction System")

st.write("Enter the patient's details below.")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=1, max_value=120, value=30)
    sex = st.selectbox("Sex", ["Male", "Female"])
    cp_option = st.selectbox(
    "Chest Pain Type",
    [
        "Typical Angina",
        "Atypical Angina",
        "Non-anginal Pain",
        "Asymptomatic"
    ]
)

cp = {
    "Typical Angina": 0,
    "Atypical Angina": 1,
    "Non-anginal Pain": 2,
    "Asymptomatic": 3
}[cp_option]

trestbps = st.number_input("Resting Blood Pressure", value=120)
chol = st.number_input("Cholesterol", value=200)
fbs = st.selectbox("Fasting Blood Sugar", ["No", "Yes"])

with col2:
    restecg_option = st.selectbox(
    "Resting ECG",
    [
        "Normal",
        "ST-T Wave Abnormality",
        "Left Ventricular Hypertrophy"
    ]
)

restecg = {
    "Normal": 0,
    "ST-T Wave Abnormality": 1,
    "Left Ventricular Hypertrophy": 2
}[restecg_option]
thalach = st.number_input("Maximum Heart Rate", value=150)
exang = st.selectbox("Exercise Induced Angina", ["No", "Yes"])
oldpeak = st.number_input("Oldpeak", value=0.0)
slope_option = st.selectbox(
    "Slope",
    [
        "Upsloping",
        "Flat",
        "Downsloping"
    ]
)
slope = {
    "Upsloping": 0,
    "Flat": 1,
    "Downsloping": 2
}[slope_option]
ca = st.selectbox(
    "Number of Major Vessels",
    [0, 1, 2, 3, 4]
)
thal_option = st.selectbox(
    "Thal",
    [
        "Normal",
        "Fixed Defect",
        "Reversible Defect"
    ]
)

thal = {
    "Normal": 0,
    "Fixed Defect": 1,
    "Reversible Defect": 2
}[thal_option]
sex = 1 if sex == "Male" else 0
fbs = 1 if fbs == "Yes" else 0
exang = 1 if exang == "Yes" else 0


if st.button("Predict"):


    data = [[
        age, sex, cp, trestbps, chol,
        fbs, restecg, thalach,
        exang, oldpeak, slope,
        ca, thal
    ]]

    prediction = model.predict(data)
    probability = model.predict_proba(data)

    if prediction[0] == 1:
        st.error("❤️ Heart Disease Detected")
        st.metric(
    label="Prediction Confidence",
    value=f"{probability[0][1]*100:.2f}%"
)
    else:
        st.success("✅ No Heart Disease")
        st.metric(
    label="Prediction Confidence",
    value=f"{probability[0][0]*100:.2f}%"
)
        st.markdown("---")
st.caption("Developed by Ashik | B.Tech Information Technology | Machine Learning Project")