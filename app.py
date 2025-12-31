import streamlit as st
import cv2
import numpy as np
from PIL import Image

from utils.image_preprocess import preprocess_image
from utils.ocr_extractor import extract_text
from utils.chart_analyzer import analyze_chart
from utils.summarizer import generate_summary

st.set_page_config(page_title="AI Financial Report Analyzer")

st.title("📊 AI Financial Document Analyzer")

uploaded_file = st.file_uploader("Upload Financial Image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    image_np = np.array(image)

    st.image(image, caption="Uploaded Document", use_container_width=True)

    processed = preprocess_image(image_np)
    text = extract_text(processed)

    st.subheader("📄 Extracted Text")
    st.text(text[:2000])

    chart_info = analyze_chart(processed)
    st.subheader("📈 Chart Analysis")
    st.json(chart_info)

    summary = generate_summary(text)
    st.subheader("🧠 AI Summary")
    st.success(summary)
