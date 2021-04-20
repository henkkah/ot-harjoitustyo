from db/db import start_db
from ui/tui import run_login_ui

db = start_db()
run_login_ui(db)
