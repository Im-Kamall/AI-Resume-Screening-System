import joblib
from src.text_cleaner import clean_text


MODEL_PATH = "models/resume_model.pkl"


def load_model():
    return joblib.load(MODEL_PATH)


def predict_category(resume_text):
    model = load_model()
    cleaned_text = clean_text(resume_text)

    prediction = model.predict([cleaned_text])[0]
    probabilities = model.predict_proba([cleaned_text])[0]

    confidence = max(probabilities) * 100

    return prediction, round(confidence, 2)


if __name__ == "__main__":
    sample_resume = """
    I have experience in Python, SQL, Pandas, NumPy,
    Machine Learning, Data Cleaning, EDA and Scikit-learn.
    """

    category, confidence = predict_category(sample_resume)

    print("Predicted Category:", category)
    print("Confidence:", confidence, "%")