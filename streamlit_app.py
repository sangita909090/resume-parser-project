import streamlit as st
from resume_parser import ResumeParser
import os

st.set_page_config(page_title="Resume Parser", layout="centered")

st.title("📄 Resume Parser App")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if uploaded_file:

    os.makedirs("uploads", exist_ok=True)

    file_path = os.path.join("uploads", uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    parser = ResumeParser(file_path)
    result = parser.parse_resume()

    st.success("Resume Parsed Successfully!")

    st.subheader("Extracted Information")
    st.json(result)
