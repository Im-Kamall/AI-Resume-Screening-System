import streamlit as st
import PyPDF2

from src.predictor import predict_category
from src.skill_extractor import extract_skills
from src.job_matcher import calculate_match_score
from src.resume_feedback import generate_feedback


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

st.sidebar.title("AI Resume Screener")
st.sidebar.write("NLP + Machine Learning project for resume analysis.")
st.sidebar.markdown("---")
st.sidebar.write("Features:")
st.sidebar.write("✅ Resume category prediction")
st.sidebar.write("✅ PDF resume upload")
st.sidebar.write("✅ Skill extraction")
st.sidebar.write("✅ Job description matching")
st.sidebar.write("✅ Resume improvement feedback")

st.title("📄 AI Resume Screening System")
st.write(
    "Analyze resumes using Natural Language Processing and Machine Learning. "
    "Upload a resume, predict job category, extract skills, calculate job match score, "
    "and receive improvement suggestions."
)

left_col, right_col = st.columns(2)

with left_col:
    st.subheader("📌 Resume Input")
    uploaded_file = st.file_uploader("Upload Resume PDF", type=["pdf"])
    resume_text = st.text_area("Or Paste Resume Text", height=300)

    if uploaded_file is not None:
        resume_text = extract_text_from_pdf(uploaded_file)
        st.success("PDF text extracted successfully.")
        with st.expander("View Extracted Resume Text"):
            st.write(resume_text)

with right_col:
    st.subheader("🎯 Job Description Input")
    job_description = st.text_area(
        "Paste Job Description",
        height=300,
        placeholder="Example: Looking for a Data Science Intern skilled in Python, SQL, Pandas, Machine Learning..."
    )

if st.button("🚀 Analyze Resume"):
    if resume_text.strip() == "":
        st.warning("Please upload a resume PDF or paste resume text.")
    else:
        category, confidence = predict_category(resume_text)
        resume_skills = extract_skills(resume_text)
        feedback = generate_feedback(resume_text, job_description)

        st.success("Resume analyzed successfully!")

        st.subheader("📊 Prediction Summary")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Predicted Category", category)

        with col2:
            st.metric("Confidence Score", f"{confidence}")

        with col3:
            st.metric("Detected Skills", len(resume_skills))

        st.subheader("🧠 Extracted Resume Skills")

        if resume_skills:
            st.write(" ".join([f"`{skill}`" for skill in resume_skills]))
        else:
            st.info("No matching skills found.")

        st.subheader("📄 Resume Statistics")

        words = resume_text.split()

        stat1, stat2, stat3 = st.columns(3)

        with stat1:
            st.metric("Total Words", len(words))

        with stat2:
            st.metric("Total Characters", len(resume_text))

        with stat3:
            st.metric("Unique Skills", len(set(resume_skills)))

        if job_description.strip() != "":
            st.subheader("🎯 Resume vs Job Description Match")

            match_score, matched_skills, missing_skills = calculate_match_score(
                resume_text,
                job_description
            )

            st.metric("Match Score", f"{match_score}%")
            st.progress(match_score / 100)

            match_col, missing_col = st.columns(2)

            with match_col:
                st.write("### ✅ Matched Skills")
                if matched_skills:
                    st.write(" ".join([f"`{skill}`" for skill in matched_skills]))
                else:
                    st.warning("No matched skills found.")

            with missing_col:
                st.write("### ❌ Missing Skills")
                if missing_skills:
                    st.write(" ".join([f"`{skill}`" for skill in missing_skills]))
                else:
                    st.success("No missing skills found from the detected job skills.")
        else:
            st.info("Add a job description to calculate resume-job match score.")

        st.subheader("💡 Resume Improvement Suggestions")

        for item in feedback:
            st.write(f"- {item}")