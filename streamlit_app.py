import streamlit as st
import os
import json

from app.services.pdf_service import extract_text
from app.services.gemini_service import generate_mcqs

st.set_page_config(
    page_title="AI Exam Prep Generator",
    page_icon="📚",
    layout="wide"
)

# ======================
# SIDEBAR
# ======================

with st.sidebar:

    st.title("📚 AI Exam Prep")

    st.markdown("---")

    st.success("AI Powered Learning")

    st.markdown("""
### Features

✅ PDF Upload

✅ PDF Text Extraction

✅ MCQ Generation

✅ Flashcards

✅ Study Plan

✅ Download Result
""")

    st.markdown("---")

    st.info("Version 1.0")

# ======================
# MAIN PAGE
# ======================

st.title("📚 AI Exam Prep Generator")

st.markdown(
    "Upload PDF and generate exam preparation material."
)

uploaded_file = st.file_uploader(
    "Choose PDF File",
    type=["pdf"]
)

if uploaded_file:

    if st.button("🚀 Generate Exam Prep"):

        with st.spinner("Processing PDF..."):

            try:

                os.makedirs(
                    "uploads",
                    exist_ok=True
                )

                file_path = os.path.join(
                    "uploads",
                    uploaded_file.name
                )

                with open(file_path, "wb") as f:
                    f.write(
                        uploaded_file.getbuffer()
                    )

                extracted_text = extract_text(
                    file_path
                )

                mcqs = generate_mcqs(
                    extracted_text
                )

                data = {
                    "filename":
                    uploaded_file.name,

                    "characters":
                    len(extracted_text),

                    "preview":
                    extracted_text[:1000],

                    "mcqs":
                    mcqs
                }

                st.success(
                    "PDF Processed Successfully"
                )

                col1, col2 = st.columns(2)

                with col1:
                    st.metric(
                        "📄 File Name",
                        data["filename"]
                    )

                with col2:
                    st.metric(
                        "📊 Characters",
                        data["characters"]
                    )

                tab1, tab2 = st.tabs(
                    [
                        "📖 Preview",
                        "❓ MCQs"
                    ]
                )

                with tab1:

                    st.subheader(
                        "PDF Preview"
                    )

                    st.text_area(
                        "Extracted Text",
                        data["preview"],
                        height=450
                    )

                with tab2:

                    st.subheader(
                        "AI Generated MCQs"
                    )

                    st.markdown(
                        data["mcqs"]
                    )

                st.download_button(
                    label="📥 Download Result",
                    data=json.dumps(
                        data,
                        indent=4
                    ),
                    file_name="exam_prep.json",
                    mime="application/json"
                )

            except Exception as e:

                st.error(
                    f"Error: {str(e)}"
                )