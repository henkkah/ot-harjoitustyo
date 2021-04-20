def ask_login_command(cmd=""):
    cmd_given = False
    while not cmd_given:
        cmd = input("1 (Olemassaoleva käyttäjä) - 2 (Uusi käyttäjä) - 3 (Sulje sovellus): ")
        if cmd == "1" or cmd == "2" or cmd == "3":
            cmd_given = True
        else:
            print("Anna komento 1, 2 tai 3")
    return cmd

def ask_budget_command(cmd=""):
    cmd_given = False
    while not cmd_given:
        cmd = input("1 (Lisää budjettirivi) - 2 (Poista budjettirivi) - 3 (Kirjaudu ulos): ")
        if cmd == "1" or cmd == "2" or cmd == "3":
            cmd_given = True
        else:
            print("Anna komento 1, 2 tai 3")
    return cmd

def handle_existing_user(db, username="", password=""):
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
    return (True, userid)

def handle_new_user(db, username="", password=""):
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
    
    return (True, userid)

def add_new_budget_row(db, userid):
    class_given = False
    while not class_given:
        classification = input("Anna luokka (Tulot/Menot/Varat/Velat): ") # To be developed: Chosen from dropdown list - cannot give incorrect value
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
    
    return (True, classification, name, amount, budget_id)

def delete_existing_budget_row(db, userid):
    id_valid = False
    while not id_valid:
        remove_id = input("Anna rivin id-numero jonka haluat poistaa: ")
        try:
            classification = db.execute("SELECT classification FROM BudgetItems WHERE userid=? AND id=?", [userid, int(remove_id)]).fetchone()[0]
            db.execute("DELETE FROM BudgetItems WHERE userid=? AND id=?", [userid, int(remove_id)])
            id_valid = True
        except:
            print("Et antanut oikeaa id:tä")
    
    return (True, classification, remove_id)

def printable_budget_by_group(group, items):
    result = ""
    result += group.upper() + ":\n"
    items = sort_budget_items_by_amount(items)
    for item in items:
        result += item[0] + max(1, (20-len(item[0])))*" " + str(item[1]) + "\n"
    return result

def printable_budget_by_group_with_ids(group, items):
    result = ""
    result += group.upper() + ":\n"
    items = sort_budget_items_by_amount(items)
    for item in items:
        result += item[0] + max(1, (20-len(item[0])))*" " + str(item[1]) + " (id: " + str(item[2]) + ")\n"
    return result

# Sorts items from highest budget amount to lowest budget amount
def sort_budget_items_by_amount(items):
    return sorted(items, key=lambda x: x[1], reverse=True)
