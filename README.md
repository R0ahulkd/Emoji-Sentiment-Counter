📊 Emoji Sentiment Counter
A simple and fun data science project that reads a CSV file of messages, extracts emojis, counts them, and visualizes their sentiment distribution (Positive, Negative, Neutral, Unknown).

This project is offline-friendly, beginner-friendly, and a unique alternative to overused datasets like Titanic or Iris.

📌 Features

Extract emojis from text messages
Count frequency of each emoji
Classify emojis into sentiment categories

Visualize:

Emoji frequency
Emoji sentiment distribution

📂 Project Structure

emoji_sentiment_counter/
│-- messages.csv        # Sample dataset
│-- emoji_counter.py    # Main script
│-- README.md           # Project documentation


📊 Example Dataset (messages.csv)
Message
I love Python 😍
Feeling sleepy 😴
That was so funny 😂
I am so sad 😢
Hello there 👋


⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/emoji-sentiment-counter.git
cd emoji-sentiment-counter
2️⃣ Install Dependencies
pip install pandas emoji matplotlib
▶️ Usage
Make sure you have messages.csv in the same folder, then run:
python emoji_counter.py
📈 Output Examples
Emoji Frequency
A bar chart showing each emoji and how often it appears.

Emoji Sentiment Distribution
A bar chart showing counts for:

✅ Positive (green)

❌ Negative (red)

⚪ Neutral (gray)

🔵 Unknown (blue)

🛠 Technologies Used
Python

pandas → Data handling

emoji → Emoji extraction

matplotlib → Visualization

🚀 Future Improvements
Automatically detect sentiment for unknown emojis

Add interactive dashboard (Streamlit/Plotly)

Support multiple languages