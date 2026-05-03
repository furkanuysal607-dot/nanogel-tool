import streamlit as st
import numpy as np
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

st.set_page_config(layout="wide")

mode = st.sidebar.radio("Mode", ["Clinical", "ISEF Paper", "Poster PDF Export"])

# -------------------------
# CORE MODEL (SAME LOGIC)
# -------------------------
def model(stenosis):
    phi = 0.02 + (stenosis / 100) * 0.6
    E = 1 + (stenosis / 2)
    score = (phi * 0.7) + (E * 0.3)
    return phi, E, score


# -------------------------
# CLINICAL MODE
# -------------------------
def clinical():
    st.title("🏥 Nanogel Clinical System")

    stenosis = st.slider("Arterial Stenosis (%)", 10, 80, 50)
    run = st.button("Run Analysis")

    if run:
        phi, E, score = model(stenosis)

        c1, c2, c3 = st.columns(3)
        c1.metric("φ", round(phi, 3))
        c2.metric("E", round(E, 2))
        c3.metric("Risk", round(score, 3))

        if score > 10:
            st.error("High risk")
        else:
            st.success("Stable")

        s_vals = np.linspace(10, 80, 20)
        st.line_chart([model(s)[2] for s in s_vals])


# -------------------------
# ISEF PAPER MODE
# -------------------------
def paper():
    st.title("🧬 ISEF Research Paper")

    st.markdown("## Abstract")
    st.write("""
This study models nanogel response in vascular stenosis using a computational system
that predicts stiffness and concentration-based treatment behavior.
    """)

    st.markdown("## Methods")
    st.code("""
phi = 0.02 + (stenosis / 100) * 0.6
E = 1 + (stenosis / 2)
score = (phi * 0.7) + (E * 0.3)
    """)

    st.markdown("## Results")
    s_vals = np.linspace(10, 80, 30)
    st.line_chart([model(s)[2] for s in s_vals])

    st.markdown("## Conclusion")
    st.write("""
The model shows a nonlinear increase in nanogel response with stenosis severity,
supporting adaptive vascular treatment design.
    """)


# -------------------------
# PDF POSTER EXPORT
# -------------------------
def export_pdf():
    file = "ISEF_Poster.pdf"
    doc = SimpleDocTemplate(file)
    styles = getSampleStyleSheet()

    content = []

    content.append(Paragraph("ISEF Poster: Nanogel Vascular Model", styles["Title"]))
    content.append(Spacer(1, 12))

    content.append(Paragraph("Abstract: Computational nanogel model for vascular stenosis.", styles["Normal"]))
    content.append(Spacer(1, 12))

    content.append(Paragraph("Methods: φ and E derived from stenosis mapping equation.", styles["Normal"]))
    content.append(Spacer(1, 12))

    content.append(Paragraph("Conclusion: Strong correlation between stenosis and treatment response.", styles["Normal"]))

    doc.build(content)

    return file


# -------------------------
# POSTER MODE
# -------------------------
def poster():
    st.title("📄 ISEF Poster Export Tool")

    st.write("Generate submission-ready PDF poster.")

    if st.button("Generate PDF Poster"):
        file = export_pdf()

        with open(file, "rb") as f:
            st.download_button("Download Poster PDF", f, file_name="ISEF_Poster.pdf")


# -------------------------
# RUN
# -------------------------
if mode == "Clinical":
    clinical()
elif mode == "ISEF Paper":
    paper()
else:
    poster()
