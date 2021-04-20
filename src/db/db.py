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
