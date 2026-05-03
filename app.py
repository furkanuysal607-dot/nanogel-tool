import streamlit as st
import numpy as np

st.title("Nanogel Optimization Tool")

stenosis = st.slider("Enter stenosis (%)", 10, 80, 50)

def predict_efficiency(phi, E, stenosis):
    return np.exp(-(phi - 0.3)**2 * 10) * np.exp(-(E - 10)**2 / 200) * (1 - stenosis/100)

def optimize(stenosis):
    phi_vals = np.linspace(0.02, 0.64, 50)
    E_vals = np.linspace(0.5, 50, 50)

    best_score = -1
    best_phi = 0
    best_E = 0

    for phi in phi_vals:
        for E in E_vals:
            score = predict_efficiency(phi, E, stenosis)

            if score > best_score:
                best_score = score
                best_phi = phi
                best_E = E

    return best_phi, best_E

if st.button("Calculate Optimal Nanogel"):
    phi, E = optimize(stenosis)

    st.write(f"Optimal stiffness (E): {round(E,2)} kPa")
    st.write(f"Optimal concentration (φ): {round(phi,3)}")

    if phi > 0.6:
        st.warning("Warning: Jamming risk")

    st.success("Calculation complete")
