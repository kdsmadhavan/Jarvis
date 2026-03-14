import sqlite3

conn = sqlite3.connect("data/memory.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS memory(
id INTEGER PRIMARY KEY,
info TEXT
)
""")

conn.commit()

def save_memory(text):

    cursor.execute("INSERT INTO memory(info) VALUES(?)",(text,))
    conn.commit()

def get_memory():

    cursor.execute("SELECT info FROM memory")

    return cursor.fetchall()
