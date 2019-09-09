from database import getdb

with getdb() as db:
    # Initial database schema
    db.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id          INT     PRIMARY KEY NOT NULL,
        dispname    TEXT                NOT NULL,
        pwhash      TEXT                NOT NULL
    );
    CREATE TABLE IF NOT EXISTS codes (
        id          INT     PRIMARY KEY NOT NULL,
        username    INT                 NOT NULL,
        language    TEXT                NOT NULL,
        title       TEXT                NOT NULL,
        contents    TEXT                NOT NULL,
        FOREIGN KEY (username) REFERENCES users(id)
    );
    """)

