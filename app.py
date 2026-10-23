import os
import psycopg2
from flask import Flask

app = Flask(__name__)

def get_connection():
    return psycopg2.connect(
        host=os.environ["DB_HOST"],
        dbname=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
    )

def init_db():
    conn = get_connection()
    with conn, conn.cursor() as cur:
        cur.execute(
            "CREATE TABLE IF NOT EXISTS visites ("
            "id SERIAL PRIMARY KEY,"
            "date_visit TIMESTAMP DEFAULT NOW())"
        )
    conn.close()

@app.route("/")
def accueil():
    conn = get_connection()
    with conn, conn.cursor() as cur:
        cur.execute("INSERT INTO visites DEFAULT VALUES")
        cur.execute("SELECT COUNT(*) FROM visites")
        total = cur.fetchone()[0]
    conn.close()
    return f"Bonjour ! Cette page a été visitée {total} fois."

if __name__ == "__main__":
    init_db()
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=os.environ.get("FLASK_DEBUG") == "1",
    )
