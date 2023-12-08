import sqlite3
from datetime import datetime
import config

CREATE_TABLE = '''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username text NOT NULL,
    password_hash text NOT NULL,
    access_lvl text NOT NULL,
    time_created datetime NOT NULL,
    last_accessed datetime NOT NULL
    );'''

INSERT_ACCOUNT = '''INSERT INTO users
(username, password_hash, access_lvl, time_created, last_accessed)
VALUES(?, ?, ?, ?, ?);'''

GET_ACCOUNT = '''SELECT password_hash, access_lvl from users WHERE username = ?'''

GET_ALL_ACCOUNTS = '''SELECT username from users'''

CLEAR_TABLE = '''DELETE FROM users;'''


def create_db():
    conn = None
    c = None
    try:
        conn = sqlite3.connect(config.DATABASE)
        c = conn.cursor()
        c.execute(CREATE_TABLE)
        conn.commit()
        return True
    except BaseException as e:
        return False
    finally:
        if c is not None:
            c.close()
        if conn is not None:
            conn.close()


def add_account(username, password_hash, access_lvl):
    conn = None
    c = None
    time_created = get_time()
    last_accessed = time_created
    try:
        conn = sqlite3.connect(config.DATABASE)
        c = conn.cursor()
        c.execute(INSERT_ACCOUNT, (username, password_hash, access_lvl, time_created, last_accessed))
        conn.commit()
        print(f"Success adding account {username}")
    except sqlite3.IntegrityError as e:
        print(f"Error adding account: {e}")
    finally:
        if c is not None:
            c.close()
        if conn is not None:
            conn.close()


def get_account(username):
    conn = None
    c = None
    try:
        conn = sqlite3.connect(config.DATABASE)
        c = conn.cursor()
        c.execute(GET_ACCOUNT, (username,))
        result = c.fetchone()
        return result if result else None
    except sqlite3.DatabaseError as e:
        print(f"Error {e}. Could not retrieve account data for {username}.")
    finally:
        if c is not None:
            c.close()
        if conn is not None:
            conn.close()


def get_all_accounts():
    conn = None
    c = None
    try:
        conn = sqlite3.connect(config.DATABASE)
        c = conn.cursor()
        c.execute(GET_ALL_ACCOUNTS)
        result = c.fetchall()
        return result if result else None
    except sqlite3.DatabaseError as e:
        print(f"Error {e}. Could not retrieve accounts.")
    finally:
        if c is not None:
            c.close()
        if conn is not None:
            conn.close()


def get_time():
    time = datetime.now()
    return time.strftime("%m/%d/%Y, %H:%M:%S")


def clear_table():
    conn = None
    c = None
    try:
        conn = sqlite3.connect(config.DATABASE)
        c = conn.cursor()
        c.execute(CLEAR_TABLE)
        conn.commit()
        c.execute('''VACUUM;''')

        print("Cleared")
    except sqlite3.DatabaseError as e:
        print(f"Error {e}. Could not retrieve accounts.")
    finally:
        if c is not None:
            c.close()
        if conn is not None:
            conn.close()

