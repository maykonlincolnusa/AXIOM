import sqlite3

def get_connection():
    return sqlite3.connect("database.db")

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_text TEXT,
            bot_response TEXT
        )
    """)
    conn.commit()
    conn.close()
