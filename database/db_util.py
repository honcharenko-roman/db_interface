import contextlib
from pathlib import Path
import sqlite3 as sql

DB_NAME: str = f'/home/roman/dasha_kurs/data.db'


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


def execute_statement(query: str, values=None):
    print(query)
    with contextlib.closing(sql.connect(DB_NAME)) as connection:
        with connection:
            with contextlib.closing(connection.cursor()) as cursor:
                cursor.execute(query, values) if values else cursor.execute(query)
                return cursor.fetchall()
