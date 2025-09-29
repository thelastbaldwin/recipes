"""Initialize SQLite database"""

import os
from sqlite3 import connect, Connection, Cursor, IntegrityError

conn: Connection | None = None
curs: Cursor | None = None

def init_user():
    curs.execute("""CREATE TABLE IF NOT EXISTS user(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE,
        username TEXT UNIQUE,
        password_hash TEXT
        )""")

def init_recipe():
    curs.execute("""CREATE TABLE IF NOT EXISTS recipe(
        recipe_id INTEGER PRIMARY KEY AUTOINCREMENT,
        owner_id INTEGER,
        name TEXT, 
        notes TEXT,
        ingredients TEXT,
        steps TEXT,
        serves INT,
        prep_time INT,
        cook_time INT, 
        FOREIGN KEY (owner_id) REFERENCES user(user_id)
        )""")

def get_db(name: str|None = None, reset: bool = False):
    """Connect to SQLite database file"""
    global conn, curs
    if conn:
        if not reset:
            return
        conn = None
    if not name:
        name = str(os.getenv("RECIPE_SQLITE_DB"))
    conn = connect(name, check_same_thread=False)
    curs = conn.cursor()

get_db()
init_user()
init_recipe()
