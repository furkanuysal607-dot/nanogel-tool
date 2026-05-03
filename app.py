import streamlit as st
import numpy as np

st.set_page_config(layout="wide")

st.markdown("""
<style>
.main {
    background-color: #0b0f19;
    color: white;
}
.block-container {
    padding-top: 2rem;
}
div[data-testid="stMetric"] {
    background-color: #111827;
    border-radius: 10px;
    padding: 10px;
}
</style>
""", unsafe_allow_html=True)

st.title("🏥 Nanogel Clinical Decision System")

st.markdown("### System Status: 🟢 Stable | Simulation Mode | Active Monitoring")

col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    st.subheader("Patient Record")

    patient_id = st.text_input("Patient ID")
    age = st.number_input("Age", 20, 100, 60)
    stenosis = st.slider("Arterial Stenosis (%)", 10, 80, 50)

    run = st.button("Run Clinical Scan")

with col2:
    st.subheader("Clinical Decision Output")

    if run:
        phi = 0.02 + (stenosis / 100) * 0.6
        E = 1 + (stenosis / 2)
        score = (phi * 0.7) + (E * 0.3)

        c1, c2, c3 = st.columns(3)
        c1.metric("Nanogel φ", round(phi, 3))
        c2.metric("Stiffness E", round(E, 2))
        c3.metric("Risk Index", round(score, 3))

        if score > 10:
            st.error("CRITICAL VASCULAR RISK")
        else:
            st.success("Stable condition")

        st.subheader("Dose-Response Curve")

        s_vals = np.linspace(10, 80, 20)
        scores = []

        for s in s_vals:
            p = 0.02 + (s / 100) * 0.6
            e = 1 + (s / 2)
            scores.append((p * 0.7) + (e * 0.3))

        st.line_chart(scores)

with col3:
    st.subheader("Live Monitor")

    st.info("Blood Flow: Simulated")
    st.info("Nanogel Delivery: Active")
    st.info("System Load: Normal")

    st.markdown("---")
    st.caption("Clinical AI v2.0 | Research Mode Enabled")
