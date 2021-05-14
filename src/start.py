from db import open_db
from gui import run_login_ui

db = open_db()
run_login_ui(db)
