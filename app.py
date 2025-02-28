import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load model
with open("cfs_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Cold-Formed Steel Load Prediction")

# Input fields
L = st.number_input("L (mm)", value=100.0)
b = st.number_input("b (mm)", value=50.0)
c = st.number_input("c (mm)", value=30.0)
t = st.number_input("t (mm)", value=2.0)
h = st.number_input("h (mm)", value=200.0)
Yield_strength = st.number_input("Yield Strength (N/mm²)", value=250.0)
Micro_Strain = st.number_input("Micro Strain", value=0.002)

# Predict button
if st.button("Predict Load"):
    input_data = np.array([[L, b, c, t, h, Yield_strength, Micro_Strain]])
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Load (kN): {prediction:.2f}")
