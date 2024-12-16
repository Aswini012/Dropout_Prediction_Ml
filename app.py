import streamlit as st
import numpy as np
import joblib

# Custom CSS for styling the app
st.markdown("""
    <style>
    /* Background for the app */
    .stApp {
        background-color: #f0f4f7;
    }

    /* Title styling */
    .title h1 {
        font-size: 48px;
        font-weight: bold;
        color: #009688;
        text-align: center;
        margin-bottom: 40px;
    }

    /* Subtle box shadow for input widgets *
    .stNumberInput, .stSelectbox {
        box-shadow: 0px 4px 8px rgba(0,0,0,0.1);
        border-radius: 8px;
        margin-bottom: 20px;
    }

    /* Button styling */
    .stButton button {
        background-color: #009688;
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 8px;
        box-shadow: 0px 4px 8px rgba(0,0,0,0.2);
        transition: background-color 0.3s ease;
    }

    /* Button hover effect */
    .stButton button:hover {
        background-color: #00796b;
    }

    /* Text area styling for results */
    .stTextArea {
        font-size: 18px;
        color: #424242;
        border: 1px solid #bdbdbd;
        padding: 20px;
        border-radius: 10px;
        background-color: #e0f7fa;
    }
    </style>
""", unsafe_allow_html=True)

# Load the model (make sure the model is correctly loaded from the path)
model = joblib.load("Dropout_pred.pkl")

# Title with custom styling
st.markdown("<div class='title'><h1>Dropout Prediction</h1></div>", unsafe_allow_html=True)



# User inputs with section header
st.header("Please enter the input to predict Dropout Risk:")

# User inputs for stock data (Price, Adj Close, Close, High, Low, Open)
student_ID = st.number_input("Enter Student_ID", min_value=0.0, max_value=1000.0, step=0.1)
Gender = st.number_input("Enter Gender(0 or 1)", min_value=0.0, max_value=1000.0, step=0.1)
Parental_Education = st.number_input("Enter Parental_Education(0,1,2,3)", min_value=0.0, max_value=1000.0, step=0.1)
Attendance_Rate = st.number_input("Enter Attendance_Rate", min_value=0.0, max_value=1000.0, step=0.1)
SocioEconomic_Status = st.number_input("Enter SocioEconomic_Status (0,1,2)", min_value=0.0, max_value=1000.0, step=0.1)
Engagement_Score = st.number_input("Enter Engagement_Score", min_value=0, max_value=100000000, step=1)
Test_Score_Median = st.number_input("Test_Score_Median", min_value=0, max_value=100000000, step=1)

# Prepare input features (Removed 'Volume' to match the model's expected input)
input_features = [[student_ID,Gender,Parental_Education,Attendance_Rate,SocioEconomic_Status,Engagement_Score,Test_Score_Median]]

# Prediction with a button
if st.button("Predict Dropout Risk"):
    prediction = model.predict(input_features)

    # Display prediction result as 'Increase' or 'Decrease' with color
    if prediction == 1:
        st.markdown("<h2 style='color: green;'>It Predicts the student is Dropout.</h2>", unsafe_allow_html=True)
    else:
        st.markdown("<h2 style='color: red;'>Not Dropout.</h2>", unsafe_allow_html=True)
