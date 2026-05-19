# Fintech Review Analytics

## Project Overview

This project analyzes customer reviews from Ethiopian mobile banking applications on the Google Play Store. The goal is to collect, clean, and analyze customer feedback in order to identify user satisfaction drivers, recurring complaints, and opportunities for product improvement.

The project focuses on three Ethiopian banking applications:

- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

The cleaned dataset produced in Task 1 will later be used for sentiment analysis, thematic analysis, database storage, and business insight generation.

---

# Task 1  Data Collection and Preprocessing

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

---

---

# Task 2 — Sentiment and Thematic Analysis

## Objective

The objective of Task 2 is to:

- Analyze customer sentiment from mobile banking reviews
- Identify recurring user experience themes
- Discover satisfaction drivers and pain points
- Prepare enriched review data for downstream analytics and database storage

---

# Sentiment Analysis

Sentiment analysis was performed using the VADER sentiment analyzer from the NLTK library.

Each review was assigned:

- A sentiment label:
  - Positive
  - Neutral
  - Negative
- A sentiment confidence score

The sentiment pipeline was implemented in:

```text
src/sentiment_analysis.py
```

## Sentiment Distribution Summary

The analysis produced the following overall sentiment distribution:

| Sentiment | Count |
|-----------|-------|
| Positive | 911 |
| Neutral | 387 |
| Negative | 202 |

The results indicate generally positive customer experiences across the three banking applications, while also highlighting recurring operational and usability issues.

---

# Thematic Analysis

Keyword-based thematic analysis was performed to identify recurring customer concerns and product strengths.

The thematic analysis pipeline included:

- Text preprocessing
- Keyword extraction
- Theme grouping
- Frequency analysis

The implementation is located in:

```text
src/thematic_analysis.py
```

## Major Themes Identified

The following business-relevant themes were identified:

- Account Access Issues
- Transaction Performance
- User Experience
- Customer Support

## Observations by Bank

### Commercial Bank of Ethiopia (CBE)

- High volume of transaction-related complaints
- Frequent mentions of customer support concerns
- Strong positive sentiment overall

### Bank of Abyssinia (BOA)

- Higher proportion of negative reviews
- Frequent login and account access complaints
- Transaction performance concerns appeared repeatedly

### Dashen Bank

- More positive feedback regarding user experience
- Login and transaction-related complaints still present
- Better overall sentiment balance compared to BOA

---

# Task 3 — PostgreSQL Database Engineering

## Objective

The objective of Task 3 is to design and implement a relational PostgreSQL database for storing processed banking review data in a production-style structure.

---

# Database Design

The database used for this project is:

```text
bank_reviews
```

The schema consists of two relational tables:

## Banks Table

Stores metadata about the banking applications.

| Column | Description |
|---|---|
| bank_id | Primary Key |
| bank_name | Bank name |
| app_name | Google Play application name |

## Reviews Table

Stores cleaned and processed review data.

| Column | Description |
|---|---|
| review_id | Primary Key |
| bank_id | Foreign Key referencing banks |
| review_text | Customer review text |
| rating | Review rating (1–5) |
| review_date | Review posting date |
| sentiment_label | Sentiment category |
| sentiment_score | Sentiment confidence score |
| identified_theme | Extracted business theme |
| source | Review source |

---

# Database Technologies

The following technologies were used:

- PostgreSQL
- pgAdmin
- psycopg2
- SQL
- python-dotenv

---

# Database Scripts

The database engineering workflow is implemented using the following scripts:

```text
scripts/
├── create_tables.py
├── insert_data.py
└── verify_database.py
```

## Schema File

```text
sql/schema.sql
```

---

# Secure Credential Management

Database credentials are managed using environment variables stored in a local `.env` file.

Sensitive credentials are excluded from GitHub using:

```text
.gitignore
```

Example environment configuration:

```env
DB_HOST=localhost
DB_NAME=bank_reviews
DB_USER=postgres
DB_PASSWORD=your_password
DB_PORT=5432
```

---

# Database Verification

Verification queries were implemented to validate:

- Review counts per bank
- Average ratings per bank
- Missing critical values
- Foreign key integrity

The verification script is located in:

```text
scripts/verify_database.py
```

---

# Updated Project Structure

```text
fintech-review-analytics/
│
├── .github/
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
├── scripts/
│   ├── create_tables.py
│   ├── insert_data.py
│   └── verify_database.py
│
├── sql/
│   └── schema.sql
│
├── src/
├── tests/
├── requirements.txt
└── README.md
```