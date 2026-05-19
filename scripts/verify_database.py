import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()


conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    port=os.getenv("DB_PORT")
)

cur = conn.cursor()


print("\nReviews Per Bank")

cur.execute("""
SELECT b.bank_name, COUNT(*)
FROM reviews r
JOIN banks b ON r.bank_id = b.bank_id
GROUP BY b.bank_name
ORDER BY b.bank_name
""")

for row in cur.fetchall():
    print(row)

print("\nAverage Rating Per Bank")

cur.execute("""
SELECT b.bank_name, ROUND(AVG(r.rating), 2)
FROM reviews r
JOIN banks b ON r.bank_id = b.bank_id
GROUP BY b.bank_name
ORDER BY b.bank_name
""")

for row in cur.fetchall():
    print(row)


print("\nNull Check")

cur.execute("""
SELECT COUNT(*)
FROM reviews
WHERE review_text IS NULL
OR rating IS NULL
""")

print(cur.fetchone())


cur.close()
conn.close()

print("\nDatabase verification completed successfully!")