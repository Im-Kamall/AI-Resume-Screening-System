import os
import joblib
import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

from src.text_cleaner import clean_text


DATA_PATH = "data/resume_dataset.csv"
MODEL_PATH = "models/resume_model.pkl"


def train_model():
    df = pd.read_csv(DATA_PATH)

    df = df[["Resume_str", "Category"]]
    df = df.drop_duplicates()

    df["Cleaned_Resume"] = df["Resume_str"].apply(clean_text)

    X = df["Cleaned_Resume"]
    y = df["Category"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    models = {
        "Logistic Regression": LogisticRegression(max_iter=1000),
        "Naive Bayes": MultinomialNB(),
        "Linear SVM": LinearSVC(max_iter=5000)
    }

    best_model = None
    best_accuracy = 0
    best_model_name = ""

    for name, classifier in models.items():
        pipeline = Pipeline([
            ("tfidf", TfidfVectorizer(max_features=5000)),
            ("classifier", classifier)
        ])

        pipeline.fit(X_train, y_train)

        y_pred = pipeline.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)

        print("=" * 60)
        print(f"Model: {name}")
        print(f"Accuracy: {accuracy:.4f}")
        print(classification_report(y_test, y_pred))

        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_model = pipeline
            best_model_name = name

    os.makedirs("models", exist_ok=True)
    joblib.dump(best_model, MODEL_PATH)

    print("=" * 60)
    print(f"Best Model: {best_model_name}")
    print(f"Best Accuracy: {best_accuracy:.4f}")
    print(f"Model saved at: {MODEL_PATH}")


if __name__ == "__main__":
    train_model()