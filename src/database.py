import sqlite3

def start_db():
    db = sqlite3.connect("budget.db")
    db.isolation_level = None

    # Create Users-table if does not exist already
    try:
        db.execute("CREATE TABLE Users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
    except:
        pass

    # Create BudgetItems-table if does not exist already
    try:
        db.execute("CREATE TABLE BudgetItems (id INTEGER PRIMARY KEY, name TEXT, amount INTEGER, classification TEXT, userid INTEGER REFERENCES Users)")
    except:
        pass
    
    return db

#####db.execute("CREATE TABLE Tuotteet (id INTEGER PRIMARY KEY, nimi TEXT, hinta INTEGER)")

#tulos = db.execute("INSERT INTO Tuotteet (nimi, hinta) VALUES ('lanttu', 4)")
#print(tulos.lastrowid)

#tuotteet = db.execute("SELECT nimi, hinta FROM Tuotteet").fetchall()
#hinta = db.execute("SELECT MAX(hinta) FROM Tuotteet").fetchone()

#hinta = db.execute("SELECT hinta FROM Tuotteet WHERE nimi=?", [nimi]).fetchone()
#db.execute("INSERT INTO Tuotteet (nimi, hinta) VALUES (?, ?)", [nimi, hinta])
