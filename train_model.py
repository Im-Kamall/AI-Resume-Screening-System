import os
import joblib
import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

from src.text_cleaner import clean_text


DATA_PATH = "data/resume_dataset.csv"
MODEL_PATH = "models/resume_model.pkl"


def train_model():
    df = pd.read_csv(DATA_PATH)

    df["Cleaned_Resume"] = df["Resume"].apply(clean_text)

    X = df["Cleaned_Resume"]
    y = df["Category"]

    model = Pipeline([
        ("tfidf", TfidfVectorizer()),
        ("classifier", LogisticRegression(max_iter=1000))
    ])

    model.fit(X, y)

    os.makedirs("models", exist_ok=True)
    joblib.dump(model, MODEL_PATH)

    print("Training completed successfully.")
    print(f"Total records used: {len(df)}")
    print(f"Categories: {df['Category'].nunique()}")
    print(f"Model saved at: {MODEL_PATH}")


if __name__ == "__main__":
    train_model()