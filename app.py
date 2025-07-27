import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("best_model.pkl")

# Configure the app
st.set_page_config(
    page_title="Employee Salary Classification",
    page_icon="🧑‍💼",
    layout="centered"
)

st.title("🧑‍💼 Employee Salary Classification App")
st.markdown("Predict whether an employee earns >50K or ≤50K based on various input features.")

# Sidebar inputs
st.sidebar.header("📋 Enter Employee Details")

# Input fields
age = st.sidebar.slider("Age", 18, 70, 30)
education = st.sidebar.selectbox("Education Level", [
    "Bachelors", "Masters", "PhD", "HS-grad", "Assoc", "Some-college"
])
occupation = st.sidebar.selectbox("Occupation", [
    "Tech-support", "Craft-repair", "Other-service", "Sales",
    "Exec-managerial", "Prof-specialty", "Handlers-cleaners", "Machine-op-inspct",
    "Adm-clerical", "Farming-fishing", "Transport-moving", "Priv-house-serv",
    "Protective-serv", "Armed-Forces"
])
hours_per_week = st.sidebar.slider("Hours Worked per Week", 1, 80, 40)
experience = st.sidebar.slider("Years of Experience", 0, 40, 5)
marital_status = st.sidebar.selectbox("Marital Status", [
    "Never-married", "Married-civ-spouse", "Divorced", "Separated", "Widowed", "Married-spouse-absent"
])
native_country = st.sidebar.selectbox("Country", [
    "United-States", "India", "Mexico", "Philippines", "Germany", "Canada", "England",
    "China", "France", "Japan", "Italy", "Other"
])
gender = st.sidebar.radio("Gender", ["Male", "Female"])

# Build input DataFrame (must match your model’s features and preprocessing)
input_df = pd.DataFrame({
    'age': [age],
    'education': [education],
    'occupation': [occupation],
    'hours-per-week': [hours_per_week],
    'experience': [experience],
    'marital-status': [marital_status],
    'native-country': [native_country],
    'gender': [gender]
})

st.write("### 🔍 Input Data Preview")
st.dataframe(input_df)

# Single prediction
if st.button("📊 Predict Salary Class"):
    prediction = model.predict(input_df)
    st.success(f"✅ Prediction: Employee is likely to earn **{prediction[0]}**")

# Batch prediction
st.markdown("---")
st.markdown("### 📂 Batch Prediction (Upload CSV)")
uploaded_file = st.file_uploader("Upload a CSV file with employee data", type="csv")

if uploaded_file is not None:
    batch_data = pd.read_csv(uploaded_file)
    st.write("📄 Uploaded Data Preview:")
    st.dataframe(batch_data.head())

    batch_preds = model.predict(batch_data)
    batch_data['PredictedClass'] = batch_preds

    st.write("✅ Prediction Results:")
    st.dataframe(batch_data.head())

    csv = batch_data.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="⬇️ Download Predictions CSV",
        data=csv,
        file_name='predicted_classes.csv',
        mime='text/csv'
    )


