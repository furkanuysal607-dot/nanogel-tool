import streamlit as st
import numpy as np

st.set_page_config(layout="wide")

st.title("Nanogel Clinical Decision System")

st.markdown("Clinical + Research Simulation Tool")

col1, col2 = st.columns([1, 2])

with col1:
    st.header("Patient Input")

    patient_id = st.text_input("Patient ID")
    stenosis = st.slider("Arterial Stenosis (%)", 10, 80, 50)

    run = st.button("Run Analysis")

with col2:
    st.header("Clinical Output")

    if run:
        phi = 0.02 + (stenosis / 100) * 0.6
        E = 1 + (stenosis / 2)
        score = (phi * 0.7) + (E * 0.3)

        c1, c2, c3 = st.columns(3)
        c1.metric("Nanogel φ", round(phi, 3))
        c2.metric("Stiffness E", round(E, 2))
        c3.metric("Risk Score", round(score, 3))

        if phi > 0.5:
            st.error("High clogging risk")
        else:
            st.success("Low risk")

        st.subheader("Dose-Response Curve")

        s_vals = np.linspace(10, 80, 20)
        scores = []

        for s in s_vals:
            p = 0.02 + (s / 100) * 0.6
            e = 1 + (s / 2)
            scores.append((p * 0.7) + (e * 0.3))

        st.line_chart(scores)
