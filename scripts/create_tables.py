import psycopg2
import os
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

with open("sql/schema.sql", "r") as file:
    sql_script = file.read()

cur.execute(sql_script)

conn.commit()

print("Tables created successfully!")

cur.close()
conn.close()