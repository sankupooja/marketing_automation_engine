from textblob import TextBlob


def get_sentiment(text: str) -> float:
    return TextBlob(text).sentiment.polarity
