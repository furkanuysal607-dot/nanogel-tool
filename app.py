import streamlit as st
import numpy as np
import pickle
import os

st.title("Nanogel Clinical Tool")

st.write("Upload your model file if it is not loaded.")

model = None

uploaded = st.file_uploader("Upload model.pkl", type=["pkl"])

if uploaded is not None:
    model = pickle.load(uploaded)

if model is not None:
    st.success("Model loaded")

    phi = st.slider("Nanogel concentration (φ)", 0.02, 0.64, 0.3)
    E = st.slider("Stiffness (E)", 0.5, 50.0, 10.0)
    stenosis = st.slider("Stenosis (%)", 10, 80, 50)

    if st.button("Predict"):
        result = model.predict([[phi, E, stenosis]])[0]
        st.subheader("Result")
        st.write(result)
else:
    st.warning("Upload model.pkl to continue")
