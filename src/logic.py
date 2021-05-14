from db import get_userid_of_username
from db import get_password_of_username
from db import add_new_user
from db import add_new_budget_row_to_db
from db import get_classification_of_budget_item
from db import delete_budget_row

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
    
    row = add_new_user(db, username, password)
    userid = row.lastrowid
    
    return (True, userid, None)

def sort_budget_items_by_amount(items):
    """Sorts items from highest budget amount to lowest budget amount.

    Args:
        items: data structures of revenues, expenses, assets and liabilities

    Returns:
        Given data sorted by amounts from highest to lowest.
    """
    
    return sorted(items, key=lambda x: x[1], reverse=True)

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

    row = add_new_budget_row_to_db(db, name, amount, classification, userid)
    budget_id = row.lastrowid
    
    return (True, classification, name, amount, budget_id)

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
