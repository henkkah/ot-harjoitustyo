from db import open_db
from tui import run_login_ui

db = open_db()
run_login_ui(db)
