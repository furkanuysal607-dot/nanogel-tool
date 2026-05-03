import streamlit as st
import pickle
import numpy as np

st.set_page_config(page_title="Nanogel Clinical Tool", layout="wide")

st.title("Nanogel Clinical Decision System")
st.caption("Doctor input → nanogel treatment prediction")

# LOAD MODEL (NOW LOCAL FILE)
import os
st.write("Files in folder:", os.listdir())
model = pickle.load(open("model.pkl", "rb"))

col1, col2 = st.columns(2)

with col1:
    st.header("Patient Input")

    patient_id = st.text_input("Patient ID")
    stenosis = st.slider("Arterial Stenosis (%)", 10, 80, 50)

    run = st.button("Generate Plan")

with col2:
    st.header("Results")

    if run:
        phi = 0.02 + (stenosis / 100) * 0.6
        E = 1 + (stenosis / 2)

        output = model.predict([[phi, E, stenosis]])[0]

        st.subheader("Recommended Parameters")
        st.write("Concentration (φ):", round(phi, 3))
        st.write("Stiffness (E):", round(E, 2))
        st.write("Model Output:", output)

        if phi > 0.5:
            st.error("High clogging risk")
        else:
            st.success("Low clogging risk")
