import sqlite3

# This text-based user interface is used in the initial phase in developing the app
# Later, graphical UI is developed

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

def start_ui(db):
    mode_given = False
    while not mode_given:
        mode = input("1 (Olemassaoleva käyttäjä); 2 (Uusi käyttäjä): ")
        if mode == "1" or mode == "2":
            mode_given = True
        else:
            print("Anna komento 1 tai 2")

    if mode == "1":
        username_given = False
        while not username_given:
            username = input("Anna käyttäjätunnus: ")
            try:
                user_id = db.execute("SELECT id FROM Users WHERE username=?", [username]).fetchone()[0]
                username_given = True
            except:
                print("Käyttäjätunnusta ei ole olemassa")
        
        password_given = False
        while not password_given:
            password = input("Anna salasana: ")
            if db.execute("SELECT password FROM Users WHERE username=?", [username]).fetchone()[0] != password:
                print("Väärä salasana")
            else:
                password_given = True
    
    elif mode == "2":
        username_unique = False
        while not username_unique:
            username = input("Luo käyttäjätunnus: ")
            try:
                if db.execute("SELECT username FROM Users WHERE username=?", [username]).fetchone()[0] == username:
                    print("Käyttäjätunnus on jo käytössä")
            except:
                username_unique = True
        
        password = input("Luo salasana: ")
        
        row = db.execute("INSERT INTO Users (username, password) VALUES (?, ?)", [username, password])
        user_id = row.lastrowid
    
    start_budget_ui(db, user_id)

def print_current_budget(revenues, expenses, assets, liabilities):
    print("---Tämänhetkinen BUDJETTI---\n")
    print("TULOT:")
    revenues = sorted(revenues, key=lambda x: x[1], reverse=True)
    [print( item[0] + (20 - len(item[0]))*" " + str(item[1]) ) for item in revenues]
    print()
    print("MENOT:")
    expenses = sorted(expenses, key=lambda x: x[1], reverse=True)
    [print( item[0] + (20 - len(item[0]))*" " + str(item[1]) ) for item in expenses]
    print()
    print("VARAT:")
    assets = sorted(assets, key=lambda x: x[1], reverse=True)
    [print( item[0] + (20 - len(item[0]))*" " + str(item[1]) ) for item in assets]
    print()
    print("VELAT:")
    liabilities = sorted(liabilities, key=lambda x: x[1], reverse=True)
    [print( item[0] + (20 - len(item[0]))*" " + str(item[1]) ) for item in liabilities]
    print()

def print_current_budget_with_ids(revenues, expenses, assets, liabilities):
    print("---Budjettirivit ja id:t---\n")
    print("TULOT:")
    revenues = sorted(revenues, key=lambda x: x[1], reverse=True)
    [print( item[0] + (20 - len(item[0]))*" " + str(item[1]) + " (id: " + str(item[2]) + ")" ) for item in revenues]
    print()
    print("MENOT:")
    expenses = sorted(expenses, key=lambda x: x[1], reverse=True)
    [print( item[0] + (20 - len(item[0]))*" " + str(item[1]) + " (id: " + str(item[2]) + ")" ) for item in expenses]
    print()
    print("VARAT:")
    assets = sorted(assets, key=lambda x: x[1], reverse=True)
    [print( item[0] + (20 - len(item[0]))*" " + str(item[1]) + " (id: " + str(item[2]) + ")" ) for item in assets]
    print()
    print("VELAT:")
    liabilities = sorted(liabilities, key=lambda x: x[1], reverse=True)
    [print( item[0] + (20 - len(item[0]))*" " + str(item[1]) + " (id: " + str(item[2]) + ")" ) for item in liabilities]
    print()
    
def start_budget_ui(db, user_id):
    budget_items = db.execute("SELECT * FROM BudgetItems WHERE userid=?", [user_id]).fetchall()
    budget_items = [(item[3], item[1], item[2], item[0]) for item in budget_items] # Items ordered: Classification, Name, Amount
    
    revenues = [(item[1], item[2], item[0]) for item in budget_items if item[0] == "Tulot"]
    expenses = [(item[1], item[2], item[0]) for item in budget_items if item[0] == "Menot"]
    assets = [(item[1], item[2], item[0]) for item in budget_items if item[0] == "Varat"]
    liabilities = [(item[1], item[2], item[0]) for item in budget_items if item[0] == "Velat"]

    print_current_budget(revenues, expenses, assets, liabilities)

    while True:
        cmd = input("1 (Lisää budjettirivi); 2 (Poista budjettirivi): ")
        
        if cmd == "1":
            classification = input("Anna luokka (Tulot/Menot/Varat/Velat): ") # Chosen from dropdown list - cannot give incorrect value
            name = input("Anna budjettirivin nimi: ")
            
            amount_valid = False
            while not amount_valid:
                amount = input("Anna budjettisumma kokonaislukuna: ")
                try:
                    amount = int(amount)
                    amount_valid = True
                except:
                    print("Annoit budjettisumman väärässä muodossa")
            
            row = db.execute("INSERT INTO BudgetItems (name, amount, classification, userid) VALUES (?, ?, ?, ?)", [name, amount, classification, user_id])
            budget_id = row.lastrowid
            if classification == "Tulot":
                revenues.append((name, amount, budget_id))
            elif classification == "Menot":
                expenses.append((name, amount, budget_id))
            elif classification == "Varat":
                assets.append((name, amount, budget_id))
            elif classification == "Velat":
                liabilities.append((name, amount, budget_id))
            
            print_current_budget(revenues, expenses, assets, liabilities)
        
        elif cmd == "2":
            print_current_budget_with_ids(revenues, expenses, assets, liabilities)
            
            id_valid = False
            while not id_valid:
                remove_id = input("Anna rivin id-numero jonka haluat poistaa: ")
                
                try:
                    classification = db.execute("SELECT classification FROM BudgetItems WHERE userid=? AND id=?", [user_id, int(remove_id)]).fetchone()[0]
                    db.execute("DELETE FROM BudgetItems WHERE userid=? AND id=?", [user_id, int(remove_id)])
                except:
                    print("Et antanut oikeaa id:tä")

            if classification == "Tulot":
                [(item[0], item[1], item[2]) for item in revenues if item[2] != remove_id]
            elif classification == "Menot":
                [(item[0], item[1], item[2]) for item in expenses if item[2] != remove_id]
            elif classification == "Varat":
                [(item[0], item[1], item[2]) for item in assets if item[2] != remove_id]
            elif classification == "Velat":
                [(item[0], item[1], item[2]) for item in liabilities if item[2] != remove_id]
            
            print_current_budget(revenues, expenses, assets, liabilities)

database = start_db()
start_ui(database)










