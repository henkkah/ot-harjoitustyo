import sqlite3

def open_db():
    """Creates database connection for the database used by the Budget App.
    
    If tables 'Users' and 'BudgetItems' don't exist already, they are created.
    
    Returns:
        Reference to the db object.
    """
    
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
    """Goes through budget items in given database and creates four data structures for different budget categories.
    
    Args:
        db: Database where budget data is stored
        userid: Id of the user currently handled
    
    Returns:
        Data structures for revenues, expenses, assets and liabilities.
    """
    
    budget_items = db.execute("SELECT * FROM BudgetItems WHERE userid=?", [userid]).fetchall()
    budget_items = [(item[3], item[1], item[2], item[0]) for item in budget_items] # Items ordered: Classification, Name, Amount, Id
    
    revenues = [(item[1], item[2], item[3]) for item in budget_items if item[0] == "Tulot"]
    expenses = [(item[1], item[2], item[3]) for item in budget_items if item[0] == "Menot"]
    assets = [(item[1], item[2], item[3]) for item in budget_items if item[0] == "Varat"]
    liabilities = [(item[1], item[2], item[3]) for item in budget_items if item[0] == "Velat"]

    return (revenues, expenses, assets, liabilities)

def get_budget_of_group(db, userid, group):
    budget_items = db.execute("SELECT * FROM BudgetItems WHERE userid=? AND classification=?", [userid, group]).fetchall()
    budget_items = [(item[1], item[2], item[0]) for item in budget_items] # Items ordered: Classification, Name, Amount, Id

    return budget_items

def get_userid_of_username(db, username):
    """Fetches userid of the given username from the given database.
    
    Args:
        db: database where data of the application is stored
        username: username of the handled user
    
    Returns:
        userid of the given username
    """
    
    return db.execute("SELECT id FROM Users WHERE username=?", [username]).fetchone()[0]

def get_password_of_username(db, username):
    """Fetches password of the given username from the given database.
    
    Args:
        db: database where data of the application is stored
        username: username of the handled user
    
    Returns:
        password of the given username
    """
    
    return db.execute("SELECT password FROM Users WHERE username=?", [username]).fetchone()[0]

def get_username_of_userid(db, userid):
    """Fetches username of the given userid from the given database.
    
    Args:
        db: database where data of the application is stored
        userid: userid of the handled user
    
    Returns:
        username of the given userid
    """
    
    return db.execute("SELECT username FROM Users WHERE id=?", [userid]).fetchone()[0]

def search_for_username(db, username):
    """Searches whether given username exists in given database.
    
    Args:
        db: database where data of the application is stored
        username: username of the handled user
    
    Returns:
        username if it exists in the database
    """
    
    return db.execute("SELECT username FROM Users WHERE username=?", [username]).fetchone()[0]

def add_new_user(db, username, password):
    """Creates new user to the database.
    
    Args:
        db: database where data of the application is stored
        username: username of the new user
        password: password of the new user
    
    Returns:
        id (of the row) of the new user created to the database
    """
    
    return db.execute("INSERT INTO Users (username, password) VALUES (?, ?)", [username, password])

def add_new_budget_row_to_db(db, name, amount, classification, userid):
    """Creates new budget row to the database.
    
    Args:
        db: database where data of the application is stored
        name: budget item name to be added
        amount: budget sum to be added
        classification: budget item classification to be added
        userid: user to which added budget row is linked
    
    Returns:
        id (of the row) of the new budget item added to the database
    """
    
    return db.execute("INSERT INTO BudgetItems (name, amount, classification, userid) VALUES (?, ?, ?, ?)", [name, amount, classification, userid])

def get_classification_of_budget_item(db, userid, id):
    """Fetches classification of the given budget item from the database.
    
    Args:
        db: database where data of the application is stored
        userid: id of the user currently handled
        id: id of the budget item queried
    
    Returns:
        id (of the row) of the budget item queried from the database
    """
    
    return db.execute("SELECT classification FROM BudgetItems WHERE userid=? AND id=?", [userid, id]).fetchone()[0]

def modify_budget_row(db, userid, modify_id, new_amount):
    """Modifies given budget row in the database.
    
    Args:
        db: database where data of the application is stored
        userid: id of the user currently handled
        modify_id: id of the budget item to be modified
        new_amount: new amount to be changed to the given budget row
    
    Returns:
        id (of the row) of the budget item modified in the database
    """
    
    db.execute("UPDATE BudgetItems SET amount=? WHERE userid=? AND id=?", [new_amount, userid, modify_id])

def delete_budget_row(db, userid, remove_id):
    """Deletes given budget row from the database.
    
    Args:
        db: database where data of the application is stored
        userid: id of the user currently handled
        remove_id: id of the budget item to be deleted
    
    Returns:
        id (of the row) of the budget item deleted from the database
    """
    
    db.execute("DELETE FROM BudgetItems WHERE userid=? AND id=?", [userid, remove_id])
