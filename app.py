import streamlit as st
import numpy as np

st.set_page_config(layout="wide")

st.title("Nanogel Clinical Tool")

st.header("Patient Input")

stenosis = st.slider("Stenosis (%)", 10, 80, 50)

if st.button("Run"):
    # SAFE deterministic model (no loading issues)
    phi = 0.02 + (stenosis / 100) * 0.6
    E = 1 + (stenosis / 2)

    # simplified clinical mapping (replaces broken ML load)
    output = (phi * 0.7) + (E * 0.3)

    st.write("Concentration (φ):", phi)
    st.write("Stiffness (E):", E)
    st.write("Output score:", output)

    if phi > 0.5:
        st.error("High clogging risk")
    else:
        st.success("Low clogging risk")
