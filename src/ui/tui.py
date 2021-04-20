from logic/logic import print_current_budget
from logic/logic import print_current_budget_with_ids

# This text-based user interface is used in the initial phase in developing the app
# Later, graphical UI is developed

def run_login_ui(db):
    cmd_given = False
    while not cmd_given:
        cmd = input("1 (Olemassaoleva käyttäjä) - 2 (Uusi käyttäjä) - 3 (Sulje sovellus): ")
        if cmd == "1" or cmd == "2" or cmd == "3":
            cmd_given = True
        else:
            print("Anna komento 1, 2 tai 3")

    if cmd == "3":
        exit()
    
    elif cmd == "1":
        username_given = False
        while not username_given:
            username = input("Anna käyttäjätunnus: ")
            try:
                userid = db.execute("SELECT id FROM Users WHERE username=?", [username]).fetchone()[0]
                username_given = True
            except:
                print("Käyttäjätunnusta ei ole olemassa")
        
        password_given = False
        while not password_given:
            password = input("Anna salasana: ")
            if db.execute("SELECT password FROM Users WHERE username=?", [username]).fetchone()[0] == password:
                password_given = True
            else:
                print("Väärä salasana")
    
    elif cmd == "2":
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
        userid = row.lastrowid
    
    run_budget_ui(db, userid)
    
def run_budget_ui(db, userid):
    budget_items = db.execute("SELECT * FROM BudgetItems WHERE userid=?", [userid]).fetchall()
    budget_items = [(item[3], item[1], item[2], item[0]) for item in budget_items] # Items ordered: Classification, Name, Amount, Id
    
    revenues = [(item[1], item[2], item[3]) for item in budget_items if item[0] == "Tulot"]
    expenses = [(item[1], item[2], item[3]) for item in budget_items if item[0] == "Menot"]
    assets = [(item[1], item[2], item[3]) for item in budget_items if item[0] == "Varat"]
    liabilities = [(item[1], item[2], item[3]) for item in budget_items if item[0] == "Velat"]

    print_current_budget(revenues, expenses, assets, liabilities)

    while True:
        cmd_given = False
        while not cmd_given:
            cmd = input("1 (Lisää budjettirivi) - 2 (Poista budjettirivi) - 3 (Kirjaudu ulos): ")
            if cmd == "1" or cmd == "2" or cmd == "3":
                cmd_given = True
            else:
                print("Anna komento 1, 2 tai 3")
        
        if cmd == "3":
            run_login_ui(db)
        
        elif cmd == "1":
            class_given = False
            while not class_given:
                classification = input("Anna luokka (Tulot/Menot/Varat/Velat): ") # Chosen from dropdown list - cannot give incorrect value
                if classification == "Tulot" or classification == "Menot" or classification == "Varat" or classification == "Velat":
                    class_given = True
                else:
                    print("Anna luokaksi Tulot, Menot, Varat tai Velat")
            
            name = input("Anna budjettirivin nimi: ")
            
            amount_valid = False
            while not amount_valid:
                amount = input("Anna budjettisumma kokonaislukuna: ")
                try:
                    amount = int(amount)
                    amount_valid = True
                except:
                    print("Annoit budjettisumman väärässä muodossa")
            
            row = db.execute("INSERT INTO BudgetItems (name, amount, classification, userid) VALUES (?, ?, ?, ?)", [name, amount, classification, userid])
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
                    classification = db.execute("SELECT classification FROM BudgetItems WHERE userid=? AND id=?", [userid, int(remove_id)]).fetchone()[0]
                    db.execute("DELETE FROM BudgetItems WHERE userid=? AND id=?", [userid, int(remove_id)])
                    id_valid = True
                except:
                    print("Et antanut oikeaa id:tä")

            if classification == "Tulot":
                revenues = [(item[0], item[1], item[2]) for item in revenues if item[2] != int(remove_id)]
            elif classification == "Menot":
                expenses = [(item[0], item[1], item[2]) for item in expenses if item[2] != int(remove_id)]
            elif classification == "Varat":
                assets = [(item[0], item[1], item[2]) for item in assets if item[2] != int(remove_id)]
            elif classification == "Velat":
                liabilities = [(item[0], item[1], item[2]) for item in liabilities if item[2] != int(remove_id)]
            
            print_current_budget(revenues, expenses, assets, liabilities)
