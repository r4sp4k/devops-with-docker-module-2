from flask import Flask, render_template, jsonify
import psycopg
import os

app = Flask(__name__)

def get_conn():
    return psycopg.connect(os.environ["DATABASE_URL"])

@app.route("/")
def index():
    with get_conn() as conn:
        clicks = conn.execute("SELECT count(*) FROM clicks").fetchone()[0]
    return render_template("index.html", clicks=clicks)

@app.route("/click", methods=["POST"])
def click():
    with get_conn() as conn:
        conn.execute("INSERT INTO clicks DEFAULT VALUES")
        conn.commit()
        clicks = conn.execute("SELECT count(*) FROM clicks").fetchone()[0]
    return jsonify(clicks=clicks)

with get_conn() as conn:
    conn.execute("CREATE TABLE IF NOT EXISTS clicks (id serial primary key, ts timestamp default now())")
    conn.commit()

app.run(host="0.0.0.0", port=5000)
