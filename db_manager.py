import os
import sqlite3
from datetime import datetime

DB_NAME = "headlines.db"


def get_db_path() -> str:
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), DB_NAME)


def init_db() -> None:
    with sqlite3.connect(get_db_path()) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS headlines (
                id INTEGER PRIMARY KEY,
                captured_at TIMESTAMP,
                title TEXT,
                source TEXT,
                sentiment REAL
            )
            """
        )
        columns = {row[1] for row in conn.execute("PRAGMA table_info(headlines)")}
        if "sentiment" not in columns:
            conn.execute("ALTER TABLE headlines ADD COLUMN sentiment REAL")


def insert_many_headlines(data_list: list[tuple[str, str, float]]) -> None:
    with sqlite3.connect(get_db_path()) as conn:
        conn.executemany("INSERT INTO headlines (captured_at, title, source, sentiment) VALUES (datetime('now'), ?, ?, ?)", data_list)    # Insert the headlines into the database using a bulk insert
        conn.commit() # Commit the transaction
    
