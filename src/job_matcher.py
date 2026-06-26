from src.skill_extractor import extract_skills


def calculate_match_score(resume_text, job_description):
    resume_skills = set(extract_skills(resume_text))
    job_skills = set(extract_skills(job_description))

    if not job_skills:
        return 0, [], []

    matched_skills = resume_skills.intersection(job_skills)
    missing_skills = job_skills.difference(resume_skills)

    score = (len(matched_skills) / len(job_skills)) * 100

    return round(score, 2), list(matched_skills), list(missing_skills)