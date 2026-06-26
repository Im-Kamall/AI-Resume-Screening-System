import streamlit as st
import PyPDF2

from src.predictor import predict_category
from src.skill_extractor import extract_skills


def extract_text_from_pdf(uploaded_file):
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""

    for page in pdf_reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return text


st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="📄",
    layout="centered"
)

st.title("AI Resume Screening System")
st.write("Upload a resume PDF or paste resume text to predict the best job category.")

uploaded_file = st.file_uploader("Upload Resume PDF", type=["pdf"])

resume_text = st.text_area("Or Paste Resume Text Here", height=250)

if uploaded_file is not None:
    resume_text = extract_text_from_pdf(uploaded_file)
    st.success("PDF text extracted successfully.")
    st.text_area("Extracted Resume Text", resume_text, height=250)

if st.button("Analyze Resume"):
    if resume_text.strip() == "":
        st.warning("Please upload a PDF or enter resume text.")
    else:
        category, confidence = predict_category(resume_text)
        skills = extract_skills(resume_text)

        st.success("Resume analyzed successfully!")

        st.subheader("Prediction Result")
        st.write(f"**Predicted Category:** {category}")
        st.write(f"**Confidence Score:** {confidence}%")

        st.subheader("Extracted Skills")
        if skills:
            for skill in skills:
                st.markdown(f"`{skill}`")
        else:
            st.write("No matching skills found.")

        st.subheader("Resume Statistics")
        words = resume_text.split()
        st.write(f"**Total Words:** {len(words)}")
        st.write(f"**Detected Skills:** {len(skills)}")