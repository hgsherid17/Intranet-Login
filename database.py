import sqlite3
from datetime import datetime
import config

CREATE_TABLE = '''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY_KEY AUTOINCREMENT
    username text NOT NULL
    password_hash text NOT NULL
    access_lvl text NOT NULL
    time_created datetime NOT NULL
    last_accessed datetime NOT NULL
    );'''

INSERT_ACCOUNT = '''INSERT INTO users
(id, username, password_hash, access_lvl, time_created, last_accessed)
VALUES("{id}", "{username}", "{password_hash}", "{access_lvl}", "{time_created}", "{last_accessed}");'''

GET_ACCOUNT = '''SELECT from users WHERE username = '{username}'
'''


def create_db():
    conn = None
    c = None
    try:
        conn = sqlite3.connect(config.DATABASE)
        c = conn.cursor()
        c.execute(CREATE_TABLE)
        conn.commit()
        return True
    except BaseException:
        return False
    finally:
        if c is not None:
            c.close()
        if conn is not None:
            conn.close()


def add_account(username, password_hash, access_lvl):
    conn = None
    c = None
    time_created = datetime.now()
    insert_query = INSERT_ACCOUNT.format(
        id,
        username,
        password_hash,
        access_lvl,
        time_created,
        time_created
    )

    try:
        conn = sqlite3.connect(config.DATABASE)
        c = conn.cursor()
        c.executemany(insert_query)
        conn.commit()
    except sqlite3.IntegrityError:
        print("Error")
    finally:
        if c is not None:
            c.close()
        if conn is not None:
            conn.close()









