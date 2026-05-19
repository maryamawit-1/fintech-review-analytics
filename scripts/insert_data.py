import os
import pandas as pd
import psycopg2
from dotenv import load_dotenv

df = pd.read_csv("data/processed/bank_reviews_clean.csv")

load_dotenv()

conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    port=os.getenv("DB_PORT")
)

cur = conn.cursor()