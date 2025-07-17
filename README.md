
# 🧠 AI Sentiment Analyzer

This web app lets you upload reviews and instantly detects whether the sentiment is **Positive**, **Negative**, or **Neutral** using a transformer-based NLP model. Perfect for analyzing customer feedback, survey responses, or social media comments.

---

## 🚀 Live Demo

👉 **[Click here to try the live app](https://ai-sentiment-analyzer-kkczqwgftyzpwxd4wv6vam.streamlit.app/)**

📂 **Test it instantly** with this sample file:  
[Download sample_reviews.csv](https://raw.githubusercontent.com/Shashankii/AI-sentiment-analyzer/main/sample_reviews.csv)

---

## 📋 How to Use the App

1. Click the live demo link above.
2. Click **“Browse files”** and upload the CSV file you just downloaded.
3. The app will show:
   - A preview of your data
   - Sentiment predictions for each review

> 🔍 Make sure your CSV has a column named: `Review`  
(Exactly like that – capital `R`)

---

## ✅ Features

- Upload your own CSV file with text reviews
- Auto-classifies each review as:
  - 👍 Positive
  - 😐 Neutral
  - 👎 Negative
- View sentiment predictions in real-time


---

## 📦 Tech Stack

- Python
- Streamlit
- Transformers (from Hugging Face)
- Pandas

---

## 🧑‍💻 Run Locally

```bash
git clone https://github.com/Shashankii/AI-sentiment-analyzer.git
cd AI-sentiment-analyzer
pip install -r requirements.txt
streamlit run sentiment_app.py


