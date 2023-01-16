
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

paieska = """SELECT * FROM automobiliai
WHERE marke LIKE ?
AND modelis LIKE ?
AND spalva LIKE ?
AND metai BETWEEN ? AND ?
AND kaina BETWEEN ? AND ?"""

while True:
    pasirinkimas = int(input("1 - įvesti automobilį\n2 - paieška\n3 - atvaizduoti automobilius\n0 - išeiti\n"))
    match pasirinkimas:
        case 1:
            print("Įveskite automobilį:")
            marke = input("Markė: ")
            modelis = input("Modelis: ")
            spalva = input("Spalva: ")
            metai = int(input("Metai: "))
            kaina = float(input("Kaina: "))
            with conn:
                c.execute("INSERT INTO automobiliai VALUES (NULL, ?, ?, ?, ?, ?)", (marke, modelis, spalva, metai, kaina))
        case 2:
            marke = input("Markė: ")
            modelis = input("Modelis: ")
            spalva = input("Spalva: ")
            metai_nuo = input("Metai nuo: ")
            metai_iki = input("Metai iki: ")
            kaina_nuo = input("Kaina nuo: ")
            kaina_iki = input("Kaina iki: ")
            with conn:
                c.execute(paieska, (marke, modelis, spalva, int(metai_nuo), int(metai_iki), float(kaina_nuo), float(kaina_iki)))
                print(c.fetchall())
        case 3:
            with conn:
                c.execute("SELECT * FROM automobiliai")
                print(c.fetchall())
        case 0:
            print("Viso gero")
            break
