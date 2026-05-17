import pandas as pd
from google_play_scraper import reviews, Sort


def scrape_reviews(app_id, bank_name, count=500):
    """
    Scrape Google Play reviews for a bank app.
    """

    result, _ = reviews(
        app_id,
        lang="en",
        country="et",
        sort=Sort.NEWEST,
        count=count,
        filter_score_with=None
    )

    records = []

    for r in result:
        records.append({
            "review_id": r.get("reviewId", ""),
            "review": r.get("content", ""),
            "rating": r.get("score", None),
            "date": r.get("at", None),
            "bank": bank_name,
            "source": "Google Play"
        })

    return pd.DataFrame(records)