import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pickle
import gdown
from reportlab.pdfgen import canvas
import os
import datetime

st.set_page_config(layout="wide")

st.title("AI Clinical Nanogel System")
st.caption("ML-based nanogel optimization for vascular stenosis")
MODEL_ID = "1sg67k74pKDllq1rsDlV3HQ-KNiQai4U4"

if not os.path.exists("model.pkl"):
    url = f"https://drive.google.com/uc?id={MODEL_ID}"
    gdown.download(url, "model.pkl", quiet=False)

rf = pickle.load(open("model.pkl", "rb"))
def predict(phi, E, stenosis):
    return rf.predict([[phi, E, stenosis]])[0]
  def optimize(stenosis):
    phi_vals = np.linspace(0.02, 0.64, 25)
    E_vals = np.linspace(0.5, 50, 25)

    best_score = -1
    best_phi = 0
    best_E = 0

    for phi in phi_vals:
        for E in E_vals:
            score = predict(phi, E, stenosis)

            if score > best_score:
                best_score = score
                best_phi = phi
                best_E = E

    return best_phi, best_E
    def create_pdf(pid, stenosis, phi, E):
    file = "report.pdf"
    c = canvas.Canvas(file)

    c.drawString(100, 800, "Nanogel Clinical Report")
    c.drawString(100, 770, f"Patient ID: {pid}")
    c.drawString(100, 750, f"Stenosis: {stenosis}%")
    c.drawString(100, 730, f"Optimal φ: {phi:.3f}")
    c.drawString(100, 710, f"Optimal E: {E:.2f}")

    c.drawString(100, 680, f"Generated: {datetime.datetime.now()}")

    c.save()
    return file
    col1, col2 = st.columns(2)

with col1:
    st.header("Patient Input")

    patient_id = st.text_input("Patient ID")
    stenosis = st.slider("Stenosis (%)", 10, 80, 50)

    run = st.button("Run Optimization")

with col2:
    st.header("Results Panel")
  if run:
    phi, E = optimize(stenosis)

    st.success("Optimization Complete")

    st.metric("Stiffness (E)", f"{E:.2f} kPa")
    st.metric("Concentration (φ)", f"{phi:.3f}")

    risk = "HIGH" if phi > 0.6 else "LOW"
    st.write("Clogging Risk:", risk)

    pdf = create_pdf(patient_id, stenosis, phi, E)

    with open(pdf, "rb") as f:
        st.download_button("Download Report", f, file_name="report.pdf")
      st.subheader("Clinical Response Curve")

s_vals = np.linspace(10, 80, 20)
phi_vals = []
E_vals = []

for s in s_vals:
    p, e = optimize(s)
    phi_vals.append(p)
    E_vals.append(e)

fig, ax1 = plt.subplots()

ax1.plot(s_vals, E_vals)
ax1.set_xlabel("Stenosis (%)")
ax1.set_ylabel("Stiffness")

ax2 = ax1.twinx()
ax2.plot(s_vals, phi_vals, linestyle="dashed")
ax2.set_ylabel("Concentration")

st.pyplot(fig)
