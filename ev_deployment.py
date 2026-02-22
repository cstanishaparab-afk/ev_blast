import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("dt_model (1).pkl")
model_columns = joblib.load("model_columns.pkl")

st.title("EV Battery Health Prediction")

# Numeric Inputs
Temperature = st.number_input("Temperature")
Poor_Cell_Design = st.number_input("Poor Cell Design (0 or 1)")
Poor_Battery_Design = st.number_input("Poor Battery Design (0 or 1)")
Short_Circuits = st.number_input("Short Circuits (0 or 1)")

# Categorical Inputs
Battery_Type = st.selectbox("Battery Type", ["Li-ion", "NiMH", "Lead Acid"])
External_Abuse = st.selectbox("External Abuse", ["Yes", "No"])
Overcharge_Overdischarge = st.selectbox("Overcharge/Overdischarge", ["Yes", "No"])
Battery_Maintenance = st.selectbox("Battery Maintenance", ["Good", "Poor"])

# Create dataframe
input_data = pd.DataFrame({
    "Temperature": [Temperature],
    "Poor_Cell_Design": [Poor_Cell_Design],
    "Poor_Battery_Design": [Poor_Battery_Design],
    "Short_Circuits": [Short_Circuits],
    "Battery_Type": [Battery_Type],
    "External_Abuse": [External_Abuse],
    "Overcharge_Overdischarge": [Overcharge_Overdischarge],
    "Battery_Maintenance": [Battery_Maintenance]
})

# Convert categorical to dummies
input_data = pd.get_dummies(input_data)

# Ensure same columns as training
input_data = input_data.reindex(columns=model_columns, fill_value=0)

# Prediction
if st.button("Predict"):
    prediction = model.predict(input_data)
    st.success(f"Predicted Battery Health: {prediction[0]}")
