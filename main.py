
import sqlite3

conn = sqlite3.connect('masinos.db')
c = conn.cursor()

with conn:
    c.execute("""CREATE TABLE IF NOT EXISTS 'automobiliai' (
'id' INTEGER NOT NULL UNIQUE,
'marke' TEXT,
'modelis' TEXT,
'spalva' TEXT,
'metai' INTEGER,
'kaina' REAL,
PRIMARY KEY("id" AUTOINCREMENT)
)""")

