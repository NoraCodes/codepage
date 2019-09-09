"""
Database handling code for the CodePage
"""
import psycopg2
import config

def getdb():
    return psycopg2.connect(
            dbname=config.DB_NAME,
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            port=config.DB_PORT
            )

