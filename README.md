# AI-sentiment-analyzer
A Streamlit app that performs sentiment analysis on user reviews using NLP


# 🧠 AI Sentiment Analyzer

This project is a simple web app that uses AI to analyze the **sentiment of text reviews** (positive, negative, or neutral) using natural language processing.

## 📂 How It Works

1. Upload a CSV file containing a column named **'Review'**
2. The app processes each review and classifies it as:
   - 👍 Positive
   - 😐 Neutral
   - 👎 Negative
3. You can see:
   - A preview of your data
   - Sentiment labels
   - Download option (coming soon)
   - Visualization of overall sentiment distribution (coming soon)

## 🚀 Live Demo

👉 [Click here to try the live app](https://ai-sentiment-analyzer-kkczqwgftyzpwxd4wv6vam.streamlit.app/)  


## 🛠 Tech Stack

- Python
- Streamlit
- Transformers (HuggingFace)
- Pandas

## 📦 Setup Instructions (for local run)

```bash
git clone https://github.com/Shashankii/AI-sentiment-analyzer.git
cd AI-sentiment-analyzer
pip install -r requirements.txt
streamlit run sentiment_app.py

