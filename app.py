import streamlit as st
import numpy as np

st.set_page_config(layout="wide")
st.markdown("""
<style>
/* App background */
.main {
    background-color: #F8FAFC;
    color: #000000;
}

/* Main title */
h1 {
    color: #1D4ED8;
    font-weight: 700;
}

/* Section titles */
h2, h3 {
    color: #0F172A;
}

/* Text */
p, div {
    color: #000000;
}

/* Metric boxes */
div[data-testid="stMetric"] {
    background-color: #E2E8F0;
    border-radius: 10px;
    padding: 10px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #F1F5F9;
}

/* Button styling */
.stButton > button {
    background-color: #1D4ED8;
    color: white;
    border-radius: 8px;
    border: none;
}

.stButton > button:hover {
    background-color: #1E40AF;
}
</style>
""", unsafe_allow_html=True)
st.title("Nanogel Clinical Decision System")

st.markdown("Clinical + Research Simulation Tool")

# -------------------------
# METHODS (ISEF SECTION)
# -------------------------
st.subheader("Methods & Model Assumptions")

st.markdown("""
This model simulates nanogel response under vascular stenosis using a computational framework.

Equations used:
- φ = 0.02 + (stenosis / 100) × 0.6  
- E = 1 + (stenosis / 2)  
- Risk Score = (φ × 0.7) + (E × 0.3)

Assumptions:
- Linear relationship between stenosis and nanogel concentration
- Tissue stiffness increases with vascular narrowing
- Risk score is a composite index (arbitrary units)

Limitations:
- Synthetic simulation (no clinical dataset)
- No patient-specific calibration
""")

# -------------------------
# INPUT + OUTPUT LAYOUT
# -------------------------
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
        c1.metric("Nanogel φ (fraction)", round(phi, 3))
        c2.metric("Stiffness E (kPa)", round(E, 2))
        c3.metric("Risk Score (a.u.)", round(score, 3))

        if score > 10:
            st.error("HIGH VASCULAR RISK")
        else:
            st.success("LOW RISK")

        # -------------------------
        # INTERPRETATION
        # -------------------------
        st.subheader("Interpretation")

        st.info("""
Higher stenosis increases nanogel concentration and tissue stiffness.
This suggests predictable vascular response suitable for adaptive delivery systems.
""")

        # -------------------------
        # ISEF GRAPH (IMPROVED)
        # -------------------------
        st.subheader("Dose-Response Curve (Stenosis vs Nanogel Response)")

        s_vals = np.linspace(10, 80, 20)
        scores = []
        phi_vals = []

        for s in s_vals:
            p = 0.02 + (s / 100) * 0.6
            e = 1 + (s / 2)
            phi_vals.append(p)
            scores.append((p * 0.7) + (e * 0.3))

        chart_data = {
            "Stenosis (%)": s_vals,
            "Nanogel φ (fraction)": phi_vals,
            "Risk Score (a.u.)": scores
        }

        st.line_chart(chart_data)
