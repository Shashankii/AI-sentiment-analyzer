
## 🧠 AI Sentiment Analyzer

This web app lets you upload reviews and instantly detects whether the sentiment is **Positive**, **Negative**, or **Neutral** using a transformer-based NLP model. Perfect for analyzing customer feedback, survey responses, or social media comments.

This project is a simple and powerful AI Sentiment Analyzer built using Python and Streamlit, leveraging transformers from Hugging Face. It allows users to analyze the sentiment of textual reviews—either manually entered or from a CSV file.


## 🚀 Live Demo

👉 **[Click here to try the live app](https://ai-sentiment-analyzer-bu469t68hmggh74smjcbvs.streamlit.app/)**

📂 **Test it instantly** with this sample file:  
[⬇️ Download Sample CSV](https://github.com/Shashankii/AI-sentiment-analyzer/blob/main/large_sample_reviews.csv)



🚀 Features

🎯 Instant Sentiment Prediction: Enter a review and get real-time prediction—Positive, Negative, or Neutral

📂 Batch Sentiment Analysis: Upload a CSV file containing a Review column to analyze sentiments for all rows

📊 Clean UI/UX: Intuitive interface designed using Streamlit for seamless interaction

🔍 Uses Pre-trained NLP Models: Built on top of Hugging Face's pipeline("sentiment-analysis")


🛠 Tech Stack

Frontend: Streamlit

Backend: Python

Model: Hugging Face Transformers (BERT-based sentiment analysis)

Libraries: transformers, pandas, streamlit, io


📸 App Preview

![Screenshot](https://github.com/Shashankii/AI-sentiment-analyzer/blob/main/app%20screenshot.png)


📁 How to Use

🔹 Option 1: Manual Input

Enter a review in the text box.
Click Analyze Sentiment.
See the sentiment label and confidence score instantly.

🔹 Option 2: Upload CSV

Prepare a CSV file with a column titled Review.
Upload the file using the provided uploader.
The app will process and display the sentiment analysis results.


💡 Use Cases

Customer feedback analysis

Social media sentiment tagging

Product review insights

Brand monitoring


🧠 Behind the Scenes

The app uses the Hugging Face pipeline() API for sentiment classification. It accepts raw text as input and outputs:
Label: Positive / Negative / Neutral
Score: Confidence value from 0 to 1
Batch processing is supported via CSV reading with pandas.










