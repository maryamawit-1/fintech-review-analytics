# Fintech Review Analytics

## Project Overview

This project analyzes customer reviews from Ethiopian mobile banking applications on the Google Play Store. The goal is to collect, clean, and analyze customer feedback in order to identify user satisfaction drivers, recurring complaints, and opportunities for product improvement.

The project focuses on three Ethiopian banking applications:

- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

The cleaned dataset produced in Task 1 will later be used for sentiment analysis, thematic analysis, database storage, and business insight generation.

---

# Task 1 — Data Collection and Preprocessing

## Objective

The objective of Task 1 is to:

- Scrape Google Play Store reviews
- Assess raw data quality
- Clean and preprocess review data
- Produce an analysis-ready dataset

---

# Data Collection Methodology

## Data Source

Reviews were collected from the Google Play Store using the Python library:

- `google-play-scraper`

## Target Applications

| Bank | App ID |
|------|--------|
| CBE | `com.combanketh.mobilebanking` |
| BOA | `com.boa.boaMobileBanking` |
| Dashen | `com.dashen.dashensuperapp` |

## Collected Fields

The following fields were collected for each review:

- Review text
- Rating (1–5)
- Review date
- Bank name
- Source

## Scraping Configuration

The scraper was configured with:

- Language: English (`lang='en'`)
- Country: Ethiopia (`country='et'`)
- Sort order: Newest reviews first
- Minimum target: 400+ reviews per bank

A total of more than 1,200 reviews were collected across the three banking applications.

---

# Data Preprocessing

The raw scraped dataset was cleaned using a preprocessing pipeline implemented in `src/preprocess.py`.

The following preprocessing steps were applied:

- Removed rows with missing review text or ratings
- Removed duplicate review IDs
- Standardized review text formatting
- Normalized dates to `YYYY-MM-DD`
- Validated rating values (1–5 only)

The preprocessing pipeline preserves review meaning while improving data consistency and quality.

---

# Project Structure

```text
fintech-review-analytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
├── src/
├── tests/
├── scripts/
└── README.md
```
---

## Output Files

### Raw Dataset

Stored in:

```text
data/raw/
```

### Cleaned Dataset

Stored in:

```text
data/processed/
```

---

## Technologies Used

- Python
- pandas
- google-play-scraper
- Jupyter Notebook
- Git & GitHub Actions