# this is the database file for the project. this functions can be found in /app.py but it is better to keep them separate for better readability.
# test
import sqlite3


def create_table():
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)"
    )
    connection.commit()
    connection.close()


def create_issue_table():
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS issues (id INTEGER PRIMARY KEY, title TEXT, description TEXT, severity TEXT, source TEXT)"
    )
    connection.commit()
    connection.close()
