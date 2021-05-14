import unittest
import sqlite3
import random
import string
from logic import handle_existing_user
from logic import handle_new_user
from logic import sort_budget_items_by_amount
from logic import add_new_budget_row
from logic import delete_existing_budget_row
from db import add_new_budget_row_to_db

class TestBudgetApp(unittest.TestCase):
    def setUp(self):
        self.db = sqlite3.connect("test.db")
        self.characters = string.ascii_lowercase
        
        self.db.isolation_level = None
        # Create Users-table if does not exist already
        try:
            self.db.execute("CREATE TABLE Users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
        except:
            pass
        # Create BudgetItems-table if does not exist already
        try:
            self.db.execute("CREATE TABLE BudgetItems (id INTEGER PRIMARY KEY, name TEXT, amount INTEGER, classification TEXT, userid INTEGER REFERENCES Users)")
        except:
            pass
        
        # Create test user
        self.testuser_username = self.create_random_username()
        self.testuser_password = self.create_random_password()
        self.testuser_userid = self.db.execute("INSERT INTO Users (username, password) VALUES (?, ?)", [self.testuser_username, self.testuser_password]).lastrowid

    # This method only helps other testing methods
    def create_random_username(self):
        random_username = ""
        for _ in range(10):
            random_username += self.characters[random.randint(0, len(self.characters)-1)]
        return random_username
    
    # This method only helps other testing methods
    def create_random_password(self):
        random_password = ""
        for _ in range(10):
            random_password += self.characters[random.randint(0, len(self.characters)-1)]
        return random_password
    
    def test_handle_existing_user_with_correct_user(self):
        random_username = self.create_random_username()
        random_password = self.create_random_password()
        self.db.execute("INSERT INTO Users (username, password) VALUES (?, ?)", [random_username, random_password])
        self.assertTrue(handle_existing_user(self.db, random_username, random_password)[0])

    def test_handle_existing_user_with_incorrect_user_1(self):
        random_username = self.create_random_username()
        random_password = self.create_random_password()
        self.assertFalse(handle_existing_user(self.db, random_username, random_password)[0])

    def test_handle_existing_user_with_incorrect_user_2(self):
        random_username = self.create_random_username()
        random_password = self.create_random_password()
        self.db.execute("INSERT INTO Users (username, password) VALUES (?, ?)", [random_username, random_password])
        self.assertFalse(handle_existing_user(self.db, random_username, self.create_random_password())[0])

    def test_handle_new_user_with_correct_user(self):
        random_username = self.create_random_username()
        random_password = self.create_random_password()
        self.assertTrue(handle_new_user(self.db, random_username, random_password)[0])
    
    def test_add_new_budget_row_with_correct_input(self):
        add_new_budget_row_to_db(self.db, "Ruoka", 350, "Menot", self.testuser_userid)
        self.assertEqual(self.db.execute("SELECT name, amount, classification FROM BudgetItems WHERE name=? and amount=? and classification=?", ["Ruoka", 350, "Menot"]).fetchall()[0], ("Ruoka", 350, "Menot"))

    def test_add_new_budget_row_with_incorrect_input(self):
        add_new_budget_row_to_db(self.db, "Ruoka", "Virhe", "Menot", self.testuser_userid)
        self.assertNotEqual(self.db.execute("SELECT name, amount, classification FROM BudgetItems WHERE name=? and amount=? and classification=?", ["Ruoka", "Virhe", "Menot"]).fetchall(), ("Ruoka", "Virhe", "Menot"))

    def test_delete_existing_budget_row_with_correct_input(self):
        remove_id = add_new_budget_row_to_db(self.db, "Ruoka", 350, "Menot", self.testuser_userid).lastrowid
        self.db.execute("DELETE FROM BudgetItems WHERE userid=? AND id=?", [self.testuser_userid, remove_id])
        self.assertNotEqual(self.db.execute("SELECT name, amount, classification FROM BudgetItems WHERE name=? and amount=? and classification=?", ["Ruoka", 350, "Menot"]).fetchall(), ("Ruoka", 350, "Menot"))
