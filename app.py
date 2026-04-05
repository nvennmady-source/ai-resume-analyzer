import streamlit as st
from resume_parser import extract_text_from_pdf
from ai_analyzer import analyze_resume

st.set_page_config(page_title="AI Resume Analyzer")

st.title("🤖 AI Resume Analyzer")

st.write("Upload your resume and get AI feedback.")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if uploaded_file:

    with st.spinner("Reading resume..."):
        text = extract_text_from_pdf(uploaded_file)

    st.success("Resume loaded!")

    if st.button("Analyze Resume"):

        with st.spinner("AI analyzing resume..."):
            result = analyze_resume(text)

        st.subheader("📊 AI Analysis")

        st.write(result)