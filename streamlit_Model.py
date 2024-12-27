import streamlit as st
import pickle
import pandas as pd

# Load the saved model
with open("E:/Documents(p)/Machine_Learning_Project/ML_PROJECTS/Streamlit project/Diabetes/diabetes_prediction_model.pkl", 'rb') as file:
    model = pickle.load(file)

# Function to make predictions
def predict_diabetes(input_data):
    # Define the column names (these should match the columns used in your model)
    columns = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 
               'BMI', 'DiabetesPedigreeFunction', 'Age']
    
    # Convert the input data into a DataFrame
    input_data_df = pd.DataFrame([input_data], columns=columns)
    
    # Make prediction
    prediction = model.predict(input_data_df)
    return prediction[0]

# Streamlit app interface
st.title("Diabetes Prediction App")
st.write("Enter the information below to predict whether a patient has diabetes:")

# Input fields for the user
Pregnancies = st.number_input('Number of Pregnancies', min_value=0, max_value=20, value=0)
Glucose = st.number_input('Glucose Concentration', min_value=0, max_value=200, value=0)
BloodPressure = st.number_input('Blood Pressure', min_value=0, max_value=150, value=0)
SkinThickness = st.number_input('Skin Thickness', min_value=0, max_value=100, value=0)
Insulin = st.number_input('Insulin Level', min_value=0, max_value=900, value=0)
BMI = st.number_input('BMI', min_value=0, max_value=60, value=0)
DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=2.5, value=0.0)
Age = st.number_input('Age', min_value=0, max_value=120, value=0)

# Create a list with the input values
input_data = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]

# Make a prediction when the button is pressed
if st.button('Predict'):
    prediction = predict_diabetes(input_data)
    
    if prediction == 1:
        st.write("The person is predicted to have diabetes.")
    else:
        st.write("The person is predicted to not have diabetes.")