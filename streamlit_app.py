import streamlit as st
import requests
import json

st.set_page_config(
page_title="AI Exam Prep Generator",
page_icon="📚",
layout="wide"
)

API_URL = "http://localhost:8000"

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

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file,
                    "application/pdf"
                )
            }

        response = requests.post(
            f"{API_URL}/pdf/upload-pdf",
            files=files
        )

        if response.status_code == 200:

            data = response.json()

            st.success("PDF Uploaded Successfully")

            # ======================
            # METRICS
            # ======================

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

            # ======================
            # TABS
            # ======================

            tab1, tab2 = st.tabs(
                [
                    "📖 Preview",
                    "❓ MCQs"
                ]
            )

            # ======================
            # PREVIEW TAB
            # ======================

            with tab1:

                st.subheader("PDF Preview")

                st.text_area(
                    "Extracted Text",
                    data["preview"],
                    height=450
                )

            # ======================
            # MCQ TAB
            # ======================

            with tab2:

                st.subheader("AI Generated MCQs")

                st.markdown(
                    data.get(
                        "mcqs",
                        "MCQs not generated yet"
                    )
                )

            # ======================
            # DOWNLOAD BUTTON
            # ======================

            st.download_button(
                label="📥 Download Result",
                data=json.dumps(
                    data,
                    indent=4
                ),
                file_name="exam_prep.json",
                mime="application/json"
            )

        else:

            st.error(
                "Backend Error"
            )

