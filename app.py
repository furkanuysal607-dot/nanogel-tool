import streamlit as st
import pickle
import numpy as np

st.title("Nanogel Clinical Tool")

# load model directly
import joblib
model = joblib.load("model.pkl")

st.header("Patient Input")

stenosis = st.slider("Stenosis (%)", 10, 80, 50)

if st.button("Run"):
    phi = 0.02 + (stenosis / 100) * 0.6
    E = 1 + (stenosis / 2)

    result = model.predict([[phi, E, stenosis]])[0]

    st.write("Concentration (φ):", phi)
    st.write("Stiffness (E):", E)
    st.write("Output:", result)
