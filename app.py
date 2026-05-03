import streamlit as st
import numpy as np

st.set_page_config(layout="wide")

st.title("Nanogel Clinical Decision System")

st.markdown("""
---
**Clinical Mode: Active** | **Research Mode: Enabled** | **Nanogel v1.0**
---
""")

col1, col2 = st.columns([1, 2])

with col1:
    st.header("Patient Panel")

    patient_id = st.text_input("Patient ID")
    stenosis = st.slider("Arterial Stenosis (%)", 10, 80, 50)

    run = st.button("Run Analysis")

with col2:
    st.header("Clinical + Research Output")

    if run:
        # clinical model
        phi = 0.02 + (stenosis / 100) * 0.6
        E = 1 + (stenosis / 2)
        score = (phi * 0.7) + (E * 0.3)

        # alerts
        st.subheader("Clinical Metrics")

        c1, c2, c3 = st.columns(3)
        c1.metric("Nanogel φ", round(phi, 3))
        c2.metric("Stiffness E", round(E, 2))
        c3.metric("Risk Score", round(score, 3))

        if phi > 0.5:
            st.error("⚠ High clogging risk detected. Adjust nanogel concentration.")
        else:
            st.success("Safe range. Stable flow predicted.")

        # research visual (ISEF part)
        st.subheader("Dose-Response Curve")

        s_vals = np.linspace(10, 80, 20)
        phi_vals = []
        score_vals = []

        for s in s_vals:
            p = 0.02 + (s / 100) * 0.6
            e = 1 + (s / 2)
            sc = (p * 0.7) + (e * 0.3)

            phi_vals.append(p)
            score_vals.append(sc)

        st.line_chart({
            "Stenosis vs φ": phi_vals,
            "Stenosis vs Score": score_vals
        })
