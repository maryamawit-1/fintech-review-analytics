import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="bank_reviews",
    user="postgres",
    password="YOUR_PASSWORD"
)

cur = conn.cursor()

print("\nReviews Per Bank")

cur.execute("""
SELECT b.bank_name, COUNT(*)
FROM reviews r
JOIN banks b ON r.bank_id = b.bank_id
GROUP BY b.bank_name
""")

for row in cur.fetchall():
    print(row)

# Average rating
print("\nAverage Rating Per Bank")

cur.execute("""
SELECT b.bank_name, ROUND(AVG(r.rating), 2)
FROM reviews r
JOIN banks b ON r.bank_id = b.bank_id
GROUP BY b.bank_name
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