
# 🧠 Internship Projects – Machine Learning Models

This repository contains the **Machine Learning Internship (Month 1) Tasks** assigned by **ARCH Technologies**.  
Both tasks demonstrate end-to-end **Machine Learning project development**, including **data preprocessing**, **model training**, **evaluation**, and **deployment** using **Streamlit**.

---

## 📁 Repository Structure

```
internship-ml-tasks/
│
├── Task1_Email_Spam_Classifier.ipynb # Jupyter notebook for Task 1
├── Task2_MNIST_Digit_Recognizer.ipynb # Jupyter notebook for Task 2
├── Spam_Emails.csv # Dataset for Task 1
├── model.pkl # Trained Logistic Regression model (Task 1)
├── vectorizer.pkl # TF-IDF vectorizer (Task 1)
├── mnist_model.pkl # Trained Logistic Regression model (Task 2)
├── streamlit_app.py # Streamlit app for Task 1
├── app.py # Streamlit app for Task 2
├── requirements.txt # Python dependencies
└── README.md # Project documentation
---


---

## ✅ Task 1: Email Spam Classification

### 🎯 Objective
Develop a machine learning model to classify emails as **Spam** or **Not Spam** using **Natural Language Processing (NLP)** techniques.

### 📊 Dataset
- **Source**: [Spam Collection Dataset](https://github.com/daanni69/internship-ml-projects-/blob/main/Spam_Emails.csv)
- **Size**: 5728 labeled email samples

### 🔹 Approach
1. **Data Preprocessing**
   - Convert text to lowercase
   - Remove punctuation & special characters
   - Tokenize & stem words
   - Transform text using **TF-IDF Vectorization**
2. **Model Training**
   - Algorithm: **Logistic Regression**
   - Achieved ~94% accuracy on the test set
3. **Evaluation**
   - Accuracy score, confusion matrix, classification report
4. **Deployment**
   - Built a **Streamlit** web app
   - User inputs email → Model predicts Spam / Not Spam
   - Deployable to **Streamlit Cloud** or **Render**

---

## ✅ Task 2: MNIST Digit Recognition

### 🎯 Objective
Classify handwritten digits (0–9) from the **Mini MNIST dataset** using a Logistic Regression model.

### 📊 Dataset
- **Source**: `load_digits()` from Scikit-learn
- **Size**: 1797 images (8×8 pixels each)
- **Classes**: Digits 0 to 9

### 🔹 Approach
1. **Data Preprocessing**
   - Flatten 8×8 images into 64 features
   - Normalize pixel values to range [0, 1]
2. **Model Training**
   - Algorithm: **Logistic Regression**
   - Achieved ~96% accuracy
3. **Evaluation**
   - Accuracy score, confusion matrix, classification report
   - Visualization of actual vs predicted digits
4. **Deployment**
   - Developed a **Streamlit** app
   - Allows interactive selection of an image and real-time prediction

---

## 🛠 Tech Stack
- **Programming Language**: Python  
- **Libraries**: Scikit-learn, Pandas, NumPy, Matplotlib, Streamlit, Joblib  
- **Techniques**: NLP preprocessing, TF-IDF vectorization, Logistic Regression, Model Evaluation  
- **Deployment**: Streamlit Cloud   
- **Version Control**: Git & GitHub

---

## 🚀 How to Run Locally

### 1️⃣ Clone Repository
```bash
git clone https://github.com/daanni69/internship-ml-tasks.git
cd internship-ml-tasks

## 👨‍💻 Author

**Daniyal Rajput**  
Machine Learning Intern — ARCH Technologies
📌 Aspiring AI Engineer | Machine Learning & NLP Enthusiast
🔗 [LinkedIn](https://www.linkedin.com/in/daniyal-rajput999/overlay/about-this-profile/?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base%3BPvHLdvceTVe9kVyJy5dxTw%3D%3D) | 📧 daaniyaal999@gmail.com



