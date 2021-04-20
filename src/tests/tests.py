import unittest
import sqlite3
import random
import string
from logic import ask_login_command
from logic import ask_budget_command
from logic import handle_existing_user
from logic import handle_new_user

class TestBudgetApp(unittest.TestCase):
    def setUp(self):
        self.db = sqlite3.connect("test.db")
        self.characters = string.ascii_lowercase
        
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

    def test_ask_login_command_with_correct_input(self):
        self.assertEqual(ask_login_command("1"), "1")

    def test_ask_budget_command_with_correct_input(self):
        self.assertEqual(ask_login_command("1"), "1")
    
    # This method only helps other testing methods
    def create_random_username(self):
        random_username = ""
        for _ in range(10):
            random_username += self.characters[random.randint(0, len(self.characters)-1)]
        return random_username
    
    # This method only helps other testing methods
    def create_random_username(self):
        random_password = ""
        for _ in range(10):
            random_password += self.characters[random.randint(0, len(self.characters)-1)]
        return random_password
    
    def test_handle_existing_user_with_correct_user(self):
        random_username = self.create_random_username()
        random_password = self.create_random_password()
        db.execute("INSERT INTO Users (username, password) VALUES (?, ?)", [random_username, random_password])
        self.assertTrue(handle_existing_user(db, random_username, random_password)[0])

    def test_handle_new_user_with_correct_user(self):
        random_username = self.create_random_username()
        random_password = self.create_random_password()
        self.assertTrue(handle_new_user(db, random_username, random_password)[0])
