import streamlit as st
from transformers import pipeline

# Title of the app
st.title("🧠 AI Sentiment Analyzer")

# Upload CSV file
uploaded_file = st.file_uploader("Upload your CSV file with a 'Review' column", type=["csv"])

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("✅ File uploaded successfully!")

        # Show data preview
        st.write("### 🔍 Preview of your data:")
        st.dataframe(df.head())

        # Check if 'Review' column exists
        if "Review" not in df.columns:
            st.error("❌ 'Review' column not found. Please upload a valid file.")
        else:
            def get_sentiment(text):
                score = TextBlob(str(text)).sentiment.polarity
                if score > 0.1:
                    return "Positive"
                elif score < -0.1:
                    return "Negative"
                else:
                    return "Neutral"


            df["Sentiment"] = df["Review"].apply(get_sentiment)
            st.write("### ✅ Sentiment Analysis Results:")
            st.dataframe(df[["Review", "Sentiment"]])

            # Downloadable result
            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="📥 Download Results as CSV",
                data=csv,
                file_name="sentiment_results.csv",
                mime="text/csv"
            )
    except Exception as e:
        st.error(f"❌ Error reading file: {e}")
