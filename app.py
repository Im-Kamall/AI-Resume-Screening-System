import streamlit as st
import PyPDF2

from src.predictor import predict_category
from src.skill_extractor import extract_skills
from src.job_matcher import calculate_match_score


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
    layout="wide"
)

st.title("📄 AI Resume Screening System")
st.write(
    "Analyze resumes using NLP and Machine Learning. "
    "Predict resume category, extract skills, and match resumes with job descriptions."
)

left_col, right_col = st.columns(2)

with left_col:
    st.subheader("Resume Input")

    uploaded_file = st.file_uploader("Upload Resume PDF", type=["pdf"])
    resume_text = st.text_area("Or Paste Resume Text", height=300)

    if uploaded_file is not None:
        resume_text = extract_text_from_pdf(uploaded_file)
        st.success("PDF text extracted successfully.")

with right_col:
    st.subheader("Job Description Input")

    job_description = st.text_area(
        "Paste Job Description",
        height=300,
        placeholder="Example: Looking for a Data Science Intern skilled in Python, SQL, Pandas, Machine Learning..."
    )

if st.button("Analyze Resume"):
    if resume_text.strip() == "":
        st.warning("Please upload a resume PDF or paste resume text.")
    else:
        category, confidence = predict_category(resume_text)
        resume_skills = extract_skills(resume_text)

        st.success("Resume analyzed successfully!")

        st.subheader("Prediction Result")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Predicted Category", category)

        with col2:
            st.metric("Confidence Score", f"{confidence}%")

        with col3:
            st.metric("Detected Skills", len(resume_skills))

        st.subheader("Extracted Resume Skills")

        if resume_skills:
            st.write(" ".join([f"`{skill}`" for skill in resume_skills]))
        else:
            st.info("No matching skills found.")

        st.subheader("Resume Statistics")
        words = resume_text.split()

        stat1, stat2 = st.columns(2)

        with stat1:
            st.write(f"**Total Words:** {len(words)}")

        with stat2:
            st.write(f"**Total Characters:** {len(resume_text)}")

        if job_description.strip() != "":
            st.subheader("Resume vs Job Description Match")

            match_score, matched_skills, missing_skills = calculate_match_score(
                resume_text,
                job_description
            )

            st.metric("Match Score", f"{match_score}%")
            st.progress(match_score / 100)

            col_match, col_missing = st.columns(2)

            with col_match:
                st.write("### Matched Skills")
                if matched_skills:
                    st.write(" ".join([f"`{skill}`" for skill in matched_skills]))
                else:
                    st.warning("No matched skills found.")

            with col_missing:
                st.write("### Missing Skills")
                if missing_skills:
                    st.write(" ".join([f"`{skill}`" for skill in missing_skills]))
                else:
                    st.success("No missing skills found from the detected job skills.")
        else:
            st.info("Add a job description to calculate resume-job match score.")