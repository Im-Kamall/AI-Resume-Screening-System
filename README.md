# 🤖 AI Resume Screening System

An AI-powered Resume Screening System built using **Python, Natural Language Processing (NLP), Machine Learning, and Streamlit**. The application predicts the job category of a resume, extracts technical skills, compares the resume against a job description, and provides personalized improvement suggestions.

---

## 🚀 Features

* 📄 Resume Category Prediction
* 📂 PDF Resume Upload
* 🧠 NLP-based Resume Cleaning
* 🏷 Skill Extraction
* 🎯 Resume vs Job Description Matching
* 📊 Match Score Visualization
* 💡 AI Resume Improvement Suggestions
* 📈 Exploratory Data Analysis (EDA)
* 🤖 Machine Learning Classification

---

## 🛠 Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* NLTK
* Streamlit
* Matplotlib
* WordCloud
* Joblib

---

## 📂 Project Structure

```text
AI_Resume_Screening_System
│
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
│
├── data
│   └── resume_dataset.csv
│
├── models
│   └── resume_model.pkl
│
├── notebooks
│   └── resume_screening_eda.ipynb
│
├── src
│   ├── predictor.py
│   ├── text_cleaner.py
│   ├── skill_extractor.py
│   ├── job_matcher.py
│   └── resume_feedback.py
│
└── assets
```

---

## 📊 Dataset

* Total Resumes: **2,484**
* Categories: **24**
* Source: Public Resume Dataset

---

## 🤖 Machine Learning Models

| Model               |   Accuracy |
| ------------------- | ---------: |
| Logistic Regression |     64.79% |
| Naive Bayes         |     54.73% |
| **Linear SVM**      | **70.42%** |

**Best Model:** Linear SVM

---

## ▶️ Installation

```bash
git clone https://github.com/Im-Kamall/AI-Resume-Screening-System.git

cd AI-Resume-Screening-System

pip install -r requirements.txt

python train_model.py

streamlit run app.py
```

---

## 📸 Screenshots

Add screenshots inside the `assets/` folder and reference them here.

---

## 📈 Future Improvements

* Deep Learning Models
* Transformer-based Resume Classification
* Top-3 Category Prediction
* Better Skill Matching
* Cloud Deployment
* ATS Resume Score
* LLM-powered Resume Feedback

---

## 👨‍💻 Author

**Kamal Solanki**

* GitHub: https://github.com/Im-Kamall
* LinkedIn: https://www.linkedin.com/in/kamalsolanki-dev
