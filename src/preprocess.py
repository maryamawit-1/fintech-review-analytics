import pandas as pd
import re


def clean_text(text):
    """
    Clean review text while preserving meaning.
    """

    if pd.isna(text):
        return ""

    text = str(text)

    
    text = re.sub(r"\s+", " ", text)

    text = text.strip()

    return text


def preprocess_reviews(df):
    """
    Perform preprocessing on scraped reviews.
    """

    df = df.copy()

    df = df.dropna(subset=["review", "rating"])

    df["review"] = df["review"].apply(clean_text)

    df = df[df["review"].str.len() > 0]

    # remove duplicate review IDs
    df = df.drop_duplicates(
        subset=["review_id"],
        keep="first"
    )

    df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")

    # validate ratings
    df = df[
        (df["rating"] >= 1) &
        (df["rating"] <= 5)
    ]

    df["rating"] = df["rating"].astype(int)

    return df