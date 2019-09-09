"""
Database handling code for the CodePage
"""
import psycopg2
import config

DATABASE = None

def getdb():
    global DATABASE
    if DATABASE is None:
        DATABASE = psycopg2.connect(
                dbname=config.DB_NAME,
                user=config.DB_USER,
                password=config.DB_PASS,
                host=config.DB_HOST,
                port=config.DB_PORT)
    return DATABASE.cursor()

