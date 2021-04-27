import sqlite3

def open_db():
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

def get_budgets_by_group(db, userid):
    budget_items = db.execute("SELECT * FROM BudgetItems WHERE userid=?", [userid]).fetchall()
    budget_items = [(item[3], item[1], item[2], item[0]) for item in budget_items] # Items ordered: Classification, Name, Amount, Id
    
    revenues = [(item[1], item[2], item[3]) for item in budget_items if item[0] == "Tulot"]
    expenses = [(item[1], item[2], item[3]) for item in budget_items if item[0] == "Menot"]
    assets = [(item[1], item[2], item[3]) for item in budget_items if item[0] == "Varat"]
    liabilities = [(item[1], item[2], item[3]) for item in budget_items if item[0] == "Velat"]

    return (revenues, expenses, assets, liabilities)

def get_userid_of_username(db, username):
    return db.execute("SELECT id FROM Users WHERE username=?", [username]).fetchone()[0]

def get_password_of_username(db, username):
    return db.execute("SELECT password FROM Users WHERE username=?", [username]).fetchone()[0]

def search_for_username(db, username):
    return db.execute("SELECT username FROM Users WHERE username=?", [username]).fetchone()[0]

def add_new_user(db, username, password):
    return db.execute("INSERT INTO Users (username, password) VALUES (?, ?)", [username, password])

def add_new_budget_row_to_db(db, name, amount, classification, userid):
    return db.execute("INSERT INTO BudgetItems (name, amount, classification, userid) VALUES (?, ?, ?, ?)", [name, amount, classification, userid])

def get_classification_of_budget_item(db, userid, remove_id):
    return db.execute("SELECT classification FROM BudgetItems WHERE userid=? AND id=?", [userid, remove_id]).fetchone()[0]

def delete_budget_row(db, userid, remove_id):
    db.execute("DELETE FROM BudgetItems WHERE userid=? AND id=?", [userid, remove_id])
