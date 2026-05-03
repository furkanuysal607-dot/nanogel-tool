import streamlit as st
import numpy as np
import pickle
import gdown
import os

st.title("Nanogel Clinical Tool")

MODEL_ID = "1sg67k74pKDllq1rsDlV3HQ-KNiQai4U4"

if not os.path.exists("model.pkl"):
    url = f"https://drive.google.com/uc?id={MODEL_ID}"
    gdown.download(url, "model.pkl", quiet=False)

model = pickle.load(open("model.pkl", "rb"))

st.header("Patient Input")

phi = st.slider("Nanogel concentration (φ)", 0.02, 0.64, 0.3)
E = st.slider("Stiffness (E)", 0.5, 50.0, 10.0)
stenosis = st.slider("Stenosis (%)", 10, 80, 50)

if st.button("Predict"):
    result = model.predict([[phi, E, stenosis]])[0]

    st.subheader("Result")
    st.write("Output:", result)
