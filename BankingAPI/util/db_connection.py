import logging

import psycopg2
from psycopg2._psycopg import OperationalError


def create_connection():
    try:
        logging.info("Database connection initializing")
        conn = psycopg2.connect(
           #removed for github
        )
        return conn
    except OperationalError as e:
        print(f"{e}")
        return conn


connection = create_connection()
