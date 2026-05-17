from nltk.sentiment import (
    SentimentIntensityAnalyzer
)

sia = SentimentIntensityAnalyzer()


def get_sentiment_score(text):
    """
    Generate VADER sentiment score.
    """

    return sia.polarity_scores(
        text
    )["compound"]


def get_sentiment_label(score):
    """
    Convert sentiment score into label.
    """

    if score >= 0.05:
        return "positive"

    elif score <= -0.05:
        return "negative"

    else:
        return "neutral"