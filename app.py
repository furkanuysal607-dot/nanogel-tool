import streamlit as st
import numpy as np

st.set_page_config(layout="wide")

st.title("Nanogel Clinical Decision System")

col1, col2 = st.columns([1, 2])

with col1:
    st.header("Patient Panel")

    patient_id = st.text_input("Patient ID")
    stenosis = st.slider("Arterial Stenosis (%)", 10, 80, 50)

    run = st.button("Run Analysis")

with col2:
    st.header("Clinical + Research Output")

    if run:
        phi = 0.02 + (stenosis / 100) * 0.6
        E = 1 + (stenosis / 2)

        score = (phi * 0.7) + (E * 0.3)

        st.subheader("Clinical Metrics")
        st.metric("Nanogel Concentration (φ)", round(phi, 3))
        st.metric("Tissue Stiffness (E)", round(E, 2))
        st.metric("Risk Score", round(score, 3))

        if phi > 0.5:
            st.error("HIGH CLOGGING RISK")
        else:
            st.success("LOW CLOGGING RISK")
