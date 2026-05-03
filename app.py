import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pickle
import gdown
from reportlab.pdfgen import canvas
import os

st.set_page_config(layout="wide")

st.title("AI Clinical Nanogel Optimization System")
st.caption("Patient-specific formulation engine based on physics-informed ML")
