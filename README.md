
# 🧠 Internship Projects: Machine Learning Models

This repository contains the **internship tasks assigned by ARCH Technologies** for the Machine Learning internship (Month 1). The tasks are focused on real-world machine learning problems such as NLP-based spam detection and image classification using MNIST digits.

## 📁 Repository Structure

```
internship-ml-tasks/
│
├── Task1_Email_Spam_Classifier.ipynb     # Jupyter notebook for email spam detection
├── Task2_MNIST_Digit_Recognizer.ipynb    # Jupyter notebook for MNIST digit classification (working..)
├── model.pkl                             # Trained Logistic Regression model for Task 1
├── vectorizer.pkl                        # TF-IDF vectorizer used in Task 1
├── streamlit_app.py                      # Streamlit app to deploy Task 1
├── requirements.txt                      # Python libraries required to run the app
└── README.md                             # Project description and usage
```

---

## ✅ Task 1: Email Spam Classification

### 🔹 Objective:
To develop a machine learning model that classifies email messages as **Spam** or **Not Spam** using natural language processing.

### 🔹 Dataset:
- **Source**: [Kaggle - Spam Collection Dataset]([https://www.kaggle.com/datasets/uciml/sms-spam-collection-datase](https://github.com/daanni69/internship-ml-projects-/blob/main/Spam_Emails.csv))
- Contains 5728 labeled email samples.

### 🔹 Approach:
1. **Data Preprocessing**
   - Convert text to lowercase
   - Remove punctuation
   - Use TF-IDF vectorizer to transform text

2. **Model**
   - **Logistic Regression**
   - Achieved ~94% accuracy
   - Model and vectorizer saved using `joblib`

3. **Deployment**
   - Developed a simple web app using **Streamlit**
   - Takes email text input and predicts spam or not
   - Ready for deployment via [Streamlit Cloud](https://share.streamlit.io)

---

## ⏳ Task 2: MNIST Digit Recognition

> To be completed later as part of Internship Task 2.

---

## 🛠️ Requirements

All dependencies are listed in the `requirements.txt` file.

```txt
streamlit
scikit-learn
pandas
joblib
```

Install using:

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run the App Locally

1. Clone this repository
2. Make sure `model.pkl` and `vectorizer.pkl` are in the root directory
3. Run the Streamlit app:

```bash
streamlit run streamlit_app.py
```

4. Open your browser at `http://localhost:8501`

---

## 👨‍💻 Author

**Daniyal Rajput**  
Machine Learning Intern — ARCH Technologies
