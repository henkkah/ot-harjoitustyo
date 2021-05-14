from db import get_userid_of_username
from db import get_password_of_username
from db import search_for_username
from db import add_new_user
from db import add_new_budget_row_to_db
from db import get_classification_of_budget_item
from db import modify_budget_row
from db import delete_budget_row
import tkinter.messagebox
import tkinter.simpledialog

'''
def ask_login_command_tui(cmd=""):
    """Asks command from user in login view.
    
    Asks command until user gives a valid input (1, 2 or 3).

    Returns:
        Command given by user (1, 2 or 3).
    """
    
    cmd_given = False
    while not cmd_given:
        cmd = input("1 (Olemassaoleva käyttäjä) - 2 (Uusi käyttäjä) - 3 (Sulje sovellus): ")
        if cmd == "1" or cmd == "2" or cmd == "3":
            cmd_given = True
        else:
            print("Anna komento 1, 2 tai 3")
    return cmd

def ask_budget_command_tui(cmd=""):
    """Asks command from user in budget view.
    
    Asks command until user gives a valid input (1, 2, 3 or 4).

    Returns:
        Command given by user (1, 2, 3 or 4).
    """
    
    cmd_given = False
    while not cmd_given:
        cmd = input("1 (Lisää budjettirivi) - 2 (Muokkaa budjettiriviä) - 3 (Poista budjettirivi) - 4 (Kirjaudu ulos): ")
        if cmd == "1" or cmd == "2" or cmd == "3" or cmd == "4":
            cmd_given = True
        else:
            print("Anna komento 1, 2, 3 tai 4")
    return cmd

def handle_existing_user(db, username="", password=""):
    """Asks username from the user and checks that username exists in the database.

    Asks also password of the user. Checks that password is correct for the corresponding username.

    Args:
        db: database where data is stored
    
    Returns:
        True (if user was authenticated successfully) & userid (of the existing user).
    """
    
    username_given = False
    while not username_given:
        username = input("Anna käyttäjätunnus: ")
        try:
            userid = get_userid_of_username(db, username)
            username_given = True
        except:
            print("Käyttäjätunnusta ei ole olemassa")
    
    password_given = False
    while not password_given:
        password = input("Anna salasana: ")
        if get_password_of_username(db, username) == password:
            password_given = True
        else:
            print("Väärä salasana")
    return (True, userid)

def handle_new_user(db, username="", password=""):
    """Asks username from the user and checks that username does not exist in the database.

    Asks also password of the user. After this, creates new user to the database.

    Args:
        db: database where data is stored
    
    Returns:
        True (if user was authenticated successfully) & userid (of the new user).
    """
    
    username_unique = False
    while not username_unique:
        username = input("Luo käyttäjätunnus: ")
        try:
            if search_for_username(db, username) == username:
                print("Käyttäjätunnus on jo käytössä")
        except:
            username_unique = True
    
    password = input("Luo salasana: ")
    
    row = add_new_user(db, username, password)
    userid = row.lastrowid
    
    return (True, userid)
'''

def handle_existing_user(db, username, password):
    """Checks that username exists in the database.

    Also checks that password is correct for the corresponding username.

    Args:
        db: database where data is stored
        username: username given by the user in gui
        password: password given by the user in gui
    
    Returns:
        True (if user was authenticated successfully) & userid (of the existing user) & error (if username of password is incorrect).
    """
    
    try:
        userid = get_userid_of_username(db, username)
    except:
        return (False, None, "Käyttäjätunnusta ei ole olemassa!")
    
    if get_password_of_username(db, username) != password:
        return (False, None, "Väärä salasana!")
    
    return (True, userid, None)

def handle_new_user(db, username, password):
    """Checks that username does not exist in the database.

    After this, creates new user to the database with the password given.

    Args:
        db: database where data is stored
        username: username given by the user in gui
        password: password given by the user in gui
    
    Returns:
        True (if user was authenticated successfully) & userid (of the new user) & error (if username of password is incorrect).
    """
    
    try:
        if search_for_username(db, username) == username:
            return (False, None, "Käyttäjätunnus on jo käytössä")
    except:
        if username == "":
            return (False, None, "Tyhjä käyttäjätunnus")
        else:
            pass
    
    row = add_new_user(db, username, password)
    userid = row.lastrowid
    
    return (True, userid, None)



def add_new_budget_row(db, userid, classification, name, amount):
    """Asks classification, budget item name and budget sum from the user until user gives valid input.

    After this, inserts new budget row with the given input to the database.

    Args:
        db: database where data is stored
        userid: id of the user currently handled

    Returns:
        (True, classification, name, amount, budget_id)
        - True, if new budget row was added successfully
        - classification of the new budget row
        - name of the budget item
        - amount of the budget row (budget sum)
        - budget_id (id of the inserted budget row)
    """
    '''
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
    '''
    row = add_new_budget_row_to_db(db, name, amount, classification, userid)
    budget_id = row.lastrowid
    
    return (True, classification, name, amount, budget_id)



def modify_existing_budget_row(db, userid):
    """Asks budget row id and new amount from the user until user gives valid input.

    After this, modifies corresponding budget row in the database.

    Args:
        db: database where data is stored
        userid: id of the user currently handled

    Returns:
        (True, classification, modify_id, new_amount)
        - True, if modified budget row was modified successfully
        - classification of the modified budget row
        - modify_id (id of the modified budget row)
        - new_amount of the modified budget row (budget sum)
    """
    
    id_valid = False
    while not id_valid:
        modify_id = input("Anna rivin id-numero jota haluat muokata: ")
        try:
            classification = get_classification_of_budget_item(db, userid, int(modify_id))
            id_valid = True
        except:
            print("Et antanut oikeaa id:tä")
    
    amount_valid = False
    while not amount_valid:
        new_amount = input("Anna uusi budjettisumma: ")
        try:
            new_amount = int(new_amount)
            amount_valid = True
        except:
            print("Et antanut budjettisummaa oikeassa muodossa")
    
    modify_budget_row(db, userid, int(modify_id), new_amount)
    return (True, classification, modify_id, new_amount)

def delete_existing_budget_row(db, userid, remove_id):
    """Asks budget row id and new amount from the user until user gives valid input.

    After this, modifies corresponding budget row in the database.

    Args:
        db: database where data is stored
        userid: id of the user currently handled

    Returns:
        (True, classification, remove_id)
        - True, if budget row was removed successfully
        - classification of the removed budget row
        - remove_id (id of the removed budget row)
    """
    
    classification = get_classification_of_budget_item(db, userid, remove_id)
    delete_budget_row(db, userid, remove_id)
    
    return (True, classification, remove_id)

def printable_budget_by_group(group, items):
    """Modifies given data into printable format.

    Args:
        group: ["Tulot", "Menot", "Varat", "Velat"]
        items: data structures of revenues, expenses, assets and liabilities

    Returns:
        Given data in printable format.
    """
    
    result = ""
    result += group.upper() + ":\n"
    items = sort_budget_items_by_amount(items)
    total_amount = 0
    max_length = 0
    for item in items:
        result += item[0] + max(1, (20-len(item[0])))*" " + str(item[1]) + "\n"
        total_amount += item[1]
        max_length = max(max_length, len(str(item[1])))
    # Also total amount showed
    result += "-"*(20+max_length) + "\n"
    result += group + " yhteensä:" + " "*5 + str(total_amount) + "\n"
    return result

def printable_budget_by_group_with_ids(group, items):
    """Modifies given data into printable format with budget row id's.

    Args:
        group: ["Tulot", "Menot", "Varat", "Velat"]
        items: data structures of revenues, expenses, assets and liabilities

    Returns:
        Given data in printable format with budget row id's.
    """
    
    result = ""
    result += group.upper() + ":\n"
    items = sort_budget_items_by_amount(items)
    for item in items:
        result += item[0] + max(1, (20-len(item[0])))*" " + str(item[1]) + " (id: " + str(item[2]) + ")\n"
    return result

def sort_budget_items_by_amount(items):
    """Sorts items from highest budget amount to lowest budget amount.

    Args:
        items: data structures of revenues, expenses, assets and liabilities

    Returns:
        Given data sorted by amounts from highest to lowest.
    """
    
    return sorted(items, key=lambda x: x[1], reverse=True)

def calculate_net(first, second):
    """Calculates net amount from the two given input data structures.

    Args:
        first: first data structure (revenues, expenses, assets or liabilities)
        second: second data structure (revenues, expenses, assets or liabilities)

    Returns:
        Net amount from the two given data structures. Also informs whether first or second group has higher total amount.
    """
    
    f_amounts = [item[1] for item in first]
    s_amounts = [item[1] for item in second]
    f_sum = sum(f_amounts)
    s_sum = sum(s_amounts)
    result = ""
    result += str(f_sum-s_sum)
    if f_sum >= s_sum:
        result += " (ylijäämä)"
    else:
        result += " (alijäämä)"
    return result
