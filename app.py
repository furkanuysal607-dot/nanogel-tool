import streamlit as st
import numpy as np

st.set_page_config(layout="wide")

mode = st.sidebar.radio("Mode", ["Clinical Dashboard", "ISEF Paper & Poster"])

# -------------------------
# CLINICAL MODE
# -------------------------
def clinical():
    st.markdown("""
    <style>
    .main { background-color: #0b0f19; color: white; }
    div[data-testid="stMetric"] { background-color: #111827; border-radius: 10px; padding: 10px; }
    </style>
    """, unsafe_allow_html=True)

    st.title("🏥 Nanogel Clinical Decision System")

    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        patient_id = st.text_input("Patient ID")
        age = st.number_input("Age", 20, 100, 60)
        stenosis = st.slider("Arterial Stenosis (%)", 10, 80, 50)
        run = st.button("Run Scan")

    with col2:
        st.subheader("Clinical Output")

        if run:
            phi = 0.02 + (stenosis / 100) * 0.6
            E = 1 + (stenosis / 2)
            score = (phi * 0.7) + (E * 0.3)

            c1, c2, c3 = st.columns(3)
            c1.metric("φ", round(phi, 3))
            c2.metric("E", round(E, 2))
            c3.metric("Risk", round(score, 3))

            if score > 10:
                st.error("CRITICAL RISK")
            else:
                st.success("STABLE")

            s_vals = np.linspace(10, 80, 20)
            scores = []

            for s in s_vals:
                p = 0.02 + (s / 100) * 0.6
                e = 1 + (s / 2)
                scores.append((p * 0.7) + (e * 0.3))

            st.line_chart(scores)

    with col3:
        st.subheader("Monitor")
        st.info("Flow: Simulated")
        st.info("System: Active")


# -------------------------
# ISEF MODE
# -------------------------
def isef():

    st.title("🧬 ISEF Research Paper: Nanogel Vascular Optimization")

    st.markdown("## Abstract")
    st.write("""
This project models nanogel-based vascular treatment optimization using a computational system 
that predicts stiffness and concentration response under varying arterial stenosis levels.
The system simulates biomedical behavior for potential application in targeted drug delivery.
    """)

    st.markdown("## Introduction")
    st.write("""
Arterial stenosis reduces blood flow efficiency and increases cardiovascular risk. 
Nanogel systems may offer adaptive delivery properties depending on vascular conditions.
This model explores computational relationships between stenosis, stiffness, and concentration.
    """)

    st.markdown("## Methods")

    st.code("""
phi = 0.02 + (stenosis / 100) * 0.6
E = 1 + (stenosis / 2)
score = (phi * 0.7) + (E * 0.3)
    """)

    st.markdown("## Results Simulation")

    s_vals = np.linspace(10, 80, 30)
    phi_vals = []
    score_vals = []

    for s in s_vals:
        p = 0.02 + (s / 100) * 0.6
        e = 1 + (s / 2)
        phi_vals.append(p)
        score_vals.append((p * 0.7) + (e * 0.3))

    st.line_chart({
        "Stenosis vs φ": phi_vals,
        "Stenosis vs Score": score_vals
    })

    st.markdown("## Conclusion")
    st.write("""
The simulation demonstrates a predictable relationship between arterial stenosis and nanogel response.
Higher stenosis increases both stiffness and treatment intensity requirements.
This supports potential adaptive drug delivery systems for vascular conditions.
    """)

    st.markdown("## Poster Download Section")
    st.info("Use screenshots of this page for ISEF poster panels: Abstract, Methods, Results, Conclusion")


# -------------------------
# RUN APP
# -------------------------
if mode == "Clinical Dashboard":
    clinical()
else:
    isef()
