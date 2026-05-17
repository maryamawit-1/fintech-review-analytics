import re

from nltk.corpus import stopwords


stop_words = set(
    stopwords.words("english")
)


def clean_text(text):
    """
    Clean text for NLP analysis.
    """

    text = str(text).lower()

    # remove special characters
    text = re.sub(
        r"[^a-zA-Z\s]",
        " ",
        text
    )

    # simple tokenization
    tokens = text.split()

    # remove stopwords
    tokens = [
        word
        for word in tokens
        if word not in stop_words
        and len(word) > 2
    ]

    return " ".join(tokens)