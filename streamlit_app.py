import streamlit as st
import joblib

# -----------------------------
# Load the model and vectorizer
# -----------------------------
@st.cache_resource
def load_model():
    model = joblib.load("model.pkl")
    vectorizer = joblib.load("vectorizer.pkl")
    return model, vectorizer

model, vectorizer = load_model()

# -----------------------------
# Streamlit App Interface
# -----------------------------
st.set_page_config(page_title="Email Spam Classifier", page_icon="📧")
st.title("📧 Email Spam Classifier")
st.markdown("This app uses a machine learning model to classify whether an email message is **Spam** or **Not Spam**.")

st.markdown("---")

# -----------------------------
# Input Section
# -----------------------------
email_input = st.text_area("📩 Paste your email content here:", height=200)

# -----------------------------
# Prediction
# -----------------------------
if st.button("🚀 Classify Email"):
    if not email_input.strip():
        st.warning("⚠️ Please enter email content before prediction.")
    else:
        # Preprocess
        processed_email = email_input.lower().strip()
        vectorized_input = vectorizer.transform([processed_email])
        prediction = model.predict(vectorized_input)[0]

        # Output
        st.markdown("### 🔍 Prediction Result:")
        if prediction == 1:
            st.error("❌ This email is classified as **Spam**.")
        else:
            st.success("✅ This email is classified as **Not Spam**.")