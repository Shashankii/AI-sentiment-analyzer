import streamlit as st
import pandas as pd
from transformers import pipeline

# Load pre-trained sentiment analysis model
classifier = pipeline("sentiment-analysis")

st.title("🧠 AI Sentiment Analyzer")

st.subheader("📝 Try it yourself")

# Text input for a single review
user_input = st.text_area("Enter a review here:")

if st.button("Analyze Sentiment"):
    if user_input:
        result = classifier(user_input)[0]
        st.success(f"Sentiment: {result['label']} (Confidence: {result['score']:.2f})")
    else:
        st.warning("Please enter a review to analyze.")

st.markdown("---")
st.markdown("### 📁 Or upload a CSV file with a 'Review' column")

# File upload
uploaded_file = st.file_uploader("Upload CSV", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    if "Review" in df.columns:
        st.write("✅ Preview of uploaded data:")
        st.dataframe(df.head())

        df["Sentiment"] = df["Review"].apply(lambda x: classifier(str(x))[0]["label"])
        st.write("📊 Sentiment Analysis Results:")
        st.dataframe(df[["Review", "Sentiment"]])
    else:
        st.error("❌ The CSV file must have a column named 'Review'")
