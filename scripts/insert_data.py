import os
import pandas as pd
import psycopg2
from dotenv import load_dotenv

load_dotenv()

df = pd.read_csv("data/processed/task2_sentiment_analysis.csv")

print(df.columns)
conn = psycopg2.connect(
    host=os.getenv("D" \
    "_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    port=os.getenv("DB_PORT")
)

cur = conn.cursor()

banks = [
    ("CBE", "Commercial Bank of Ethiopia Mobile"),
    ("BOA", "Bank of Abyssinia Mobile"),
    ("Dashen", "Dashen Super App")
]

for bank_name, app_name in banks:
    cur.execute("""
        INSERT INTO banks (bank_name, app_name)
        VALUES (%s, %s)
        ON CONFLICT (bank_name) DO NOTHING
    """, (bank_name, app_name))

conn.commit()

print("Banks inserted successfully!")


cur.execute("""
    SELECT bank_id, bank_name
    FROM banks
""")

bank_mapping = {
    bank_name: bank_id
    for bank_id, bank_name in cur.fetchall()
}

print("Bank mapping loaded!")


for _, row in df.iterrows():

    bank_id = bank_mapping.get(row['bank'])

    cur.execute("""
        INSERT INTO reviews (
            bank_id,
            review_text,
            rating,
            review_date,
            sentiment_label,
            sentiment_score,
            identified_theme,
            source
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        bank_id,
        row['review'],
        int(row['rating']),
        row['date'],
        row['sentiment_label'],
        float(row['sentiment_score']),
        row['identified_theme'],
        row['source']
    ))

conn.commit()

print("Review data inserted successfully!")


cur.close()
conn.close()

print("Database connection closed.")