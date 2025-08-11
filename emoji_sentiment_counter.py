import pandas as pd
import emoji
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['font.family'] = 'Segoe UI Emoji'

EMOJI_SENTIMENT = {
    '😍': 'Positive', '😄': 'Positive', '😊': 'Positive', '😌': 'Positive',
    '👍': 'Positive', '🎉': 'Positive', '😂': 'Positive', '😅': 'Positive',
    '😢': 'Negative', '😭': 'Negative', '😡': 'Negative', '😔': 'Negative',
    '😴': 'Neutral', '👋': 'Neutral', '🤔': 'Neutral'
}

def extract_emojis(text):
    if not isinstance(text, str):
        return []
    return [d['emoji'] for d in emoji.emoji_list(text)]

def count_emojis_in_df(df, text_col='Message'):
    df['emojis'] = df[text_col].fillna('').apply(extract_emojis)
    all_emojis = [e for sub in df['emojis'] for e in sub]
    return Counter(all_emojis)

def emoji_sentiment_counts(emoji_counter):
    sent_counts = Counter()
    for e, cnt in emoji_counter.items():
        sentiment = EMOJI_SENTIMENT.get(e, 'Unknown')
        sent_counts[sentiment] += cnt
    return sent_counts

def plot_counter(counter, title):
    if not counter:
        return
    s = pd.Series(dict(counter)).sort_values(ascending=False)
    colors = []
    for e in s.index:
        sentiment = EMOJI_SENTIMENT.get(e, 'Unknown')
        if sentiment == 'Positive':
            colors.append('green')
        elif sentiment == 'Negative':
            colors.append('red')
        elif sentiment == 'Neutral':
            colors.append('gray')
        else:
            colors.append('blue')
    s.plot(kind='bar', color=colors, figsize=(7,4))
    plt.title(title)
    plt.ylabel("Count")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

df = pd.read_csv("messages.csv")
emoji_counts = count_emojis_in_df(df)
print("Emoji Counts:", emoji_counts)
plot_counter(emoji_counts, "Emoji Frequency")

sentiment_counts = emoji_sentiment_counts(emoji_counts)
print("Sentiment Counts:", sentiment_counts)
plot_counter(sentiment_counts, "Emoji Sentiment Distribution")