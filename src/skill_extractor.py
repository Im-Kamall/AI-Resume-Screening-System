SKILLS = [
    "python", "sql", "pandas", "numpy", "machine learning",
    "deep learning", "tensorflow", "pytorch", "nlp",
    "computer vision", "excel", "power bi", "tableau",
    "java", "spring boot", "flask", "django", "react",
    "javascript", "html", "css", "cybersecurity", "linux"
]


def extract_skills(text):
    text = text.lower()
    found_skills = []

    for skill in SKILLS:
        if skill in text:
            found_skills.append(skill)

    return found_skills