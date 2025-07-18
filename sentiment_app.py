import streamlit as st
import pandas as pd
import joblib

# Load pre-trained sentiment analysis model
classifier = joblib.load("sentiment_model.pkl")  # ✅ Make sure this file exists

st.set_page_config(page_title="AI Sentiment Analyzer", layout="centered")

st.title("🧠 AI Sentiment Analyzer")
st.subheader("📝 Try it yourself")

# Text input for a single review
user_input = st.text_area("Enter a review here:")

if st.button("Analyze Sentiment"):
    if user_input:
        result = classifier.predict([user_input])[0]
        st.success(f"Sentiment: {result}")
    else:
        st.warning("Please enter some text to analyze.")

# Divider
st.markdown("---")

# Upload CSV section
st.subheader("📂 Or upload a CSV file with a 'Review' column")
uploaded_file = st.file_uploader("Upload CSV", type="csv")

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        if "Review" in df.columns:
            df["Predicted Sentiment"] = classifier.predict(df["Review"])
            st.write("Predictions:")
            st.dataframe(df[["Review", "Predicted Sentiment"]])
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("Download Results as CSV", csv, "predictions.csv", "text/csv")
        else:
            st.error("CSV must contain a 'Review' column.")
    except Exception as e:
        st.error(f"Error reading file: {e}")
