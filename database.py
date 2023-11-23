import sqlite3
from datetime import datetime

def create_db():
    try:
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        """CREATE TABLE IF NOT EXISTS users 
        (
        id integer PRIMARY_KEY
        username text
        password_hash text
        access_lvl test
        );"""




