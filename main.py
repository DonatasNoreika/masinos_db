
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
            marke = input("Markė: ") + "%"
            modelis = input("Modelis: ") + "%"
            spalva = input("Spalva: ") + "%"
            metai_nuo = input("Metai nuo: ")
            metai_nuo = metai_nuo if metai_nuo else 1900
            metai_iki = input("Metai iki: ")
            metai_iki = metai_iki if metai_iki else 2100
            kaina_nuo = input("Kaina nuo: ")
            kaina_nuo = kaina_nuo if kaina_nuo else 0
            kaina_iki = input("Kaina iki: ")
            kaina_iki = kaina_iki if kaina_iki else 10000000
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
