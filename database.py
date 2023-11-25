import sqlite3
from datetime import datetime

def create_db():
    try:
        conn = sqlite3.connect('users.db')
        c = conn.cursor()

        '''CREATE TABLE IF NOT EXISTS users 
        (
        id INTEGER PRIMARY_KEY AUTOINCREMENT
        username text
        password_hash text
        access_lvl text
        );'''
    except BaseException e:





