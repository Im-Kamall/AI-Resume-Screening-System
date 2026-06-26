from src.skill_extractor import extract_skills


def generate_feedback(resume_text, job_description=""):
    skills = extract_skills(resume_text)
    feedback = []

    if len(resume_text.split()) < 150:
        feedback.append("Your resume looks short. Add more project details, skills, and achievements.")

    if not skills:
        feedback.append("Add more technical skills such as Python, SQL, Machine Learning, Git, or cloud tools.")

    if "python" not in skills:
        feedback.append("Add Python if you are targeting Data Science or AI/ML roles.")

    if "sql" not in skills:
        feedback.append("Add SQL because it is important for Data Science and Analytics roles.")

    if "machine learning" not in skills:
        feedback.append("Add Machine Learning projects if you are targeting ML/Data Science roles.")

    if "git" not in skills and "github" not in skills:
        feedback.append("Add Git/GitHub to show version control and project collaboration skills.")

    if job_description.strip():
        job_skills = extract_skills(job_description)
        missing = set(job_skills) - set(skills)

        if missing:
            feedback.append("Improve your resume by adding these missing job skills: " + ", ".join(missing))

    if not feedback:
        feedback.append("Your resume looks well aligned with the detected skills and job description.")

    return feedback