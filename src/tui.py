from logic import ask_login_command
from logic import ask_budget_command
from logic import handle_existing_user
from logic import handle_new_user
from logic import add_new_budget_row
from logic import modify_existing_budget_row
from logic import delete_existing_budget_row
from logic import printable_budget_by_group
from logic import printable_budget_by_group_with_ids
from logic import calculate_net
from db import get_budgets_by_group

# This text user interface (tui) is used in the initial phase in developing the app.
# Later, graphical user interface (gui) is developed.

def run_login_ui(db):
    cmd = ask_login_command()

    if cmd == "1":
        success, userid = handle_existing_user(db)
        if success:
            run_budget_ui(db, userid)
    
    elif cmd == "2":
        success, userid = handle_new_user(db)
        if success:
            run_budget_ui(db, userid)
    
    elif cmd == "3":
        exit()
    
def run_budget_ui(db, userid):
    revenues, expenses, assets, liabilities = get_budgets_by_group(db, userid)
    
    print("\n---Tämänhetkinen BUDJETTI---\n")
    [print(printable_budget_by_group(group, item)) for (group, item) in [("Tulot", revenues), ("Menot", expenses), ("Varat", assets), ("Velat", liabilities)]]
    print("Nettotulot:", calculate_net(revenues, expenses))
    print("Nettovarat:", calculate_net(assets, liabilities) + "\n")

    while True:
        cmd = ask_budget_command()

        if cmd == "1":
            success, classification, name, amount, budget_id = add_new_budget_row(db, userid)
            if success:
                if classification == "Tulot":
                    revenues.append((name, amount, budget_id))
                elif classification == "Menot":
                    expenses.append((name, amount, budget_id))
                elif classification == "Varat":
                    assets.append((name, amount, budget_id))
                elif classification == "Velat":
                    liabilities.append((name, amount, budget_id))
                
                print("\n---Tämänhetkinen BUDJETTI---\n")
                [print(printable_budget_by_group(group, item)) for (group, item) in [("Tulot", revenues), ("Menot", expenses), ("Varat", assets), ("Velat", liabilities)]]
                print("Nettotulot:", calculate_net(revenues, expenses))
                print("Nettovarat:", calculate_net(assets, liabilities) + "\n")
        
        elif cmd == "2":
            print("---Budjettirivit ja id:t---")
            [print(printable_budget_by_group_with_ids(group, item)) for (group, item) in [("Tulot", revenues), ("Menot", expenses), ("Varat", assets), ("Velat", liabilities)]]
            
            success, classification, modify_id, new_amount = modify_existing_budget_row(db, userid)
            if success:
                revenues, expenses, assets, liabilities = get_budgets_by_group(db, userid)
                
                print("\n---Tämänhetkinen BUDJETTI---\n")
                [print(printable_budget_by_group(group, item)) for (group, item) in [("Tulot", revenues), ("Menot", expenses), ("Varat", assets), ("Velat", liabilities)]]
                print("Nettotulot:", calculate_net(revenues, expenses))
                print("Nettovarat:", calculate_net(assets, liabilities) + "\n")
        
        elif cmd == "3":
            print("---Budjettirivit ja id:t---")
            [print(printable_budget_by_group_with_ids(group, item)) for (group, item) in [("Tulot", revenues), ("Menot", expenses), ("Varat", assets), ("Velat", liabilities)]]
            
            success, classification, remove_id = delete_existing_budget_row(db, userid)
            if success:
                if classification == "Tulot":
                    revenues = [(item[0], item[1], item[2]) for item in revenues if item[2] != int(remove_id)]
                elif classification == "Menot":
                    expenses = [(item[0], item[1], item[2]) for item in expenses if item[2] != int(remove_id)]
                elif classification == "Varat":
                    assets = [(item[0], item[1], item[2]) for item in assets if item[2] != int(remove_id)]
                elif classification == "Velat":
                    liabilities = [(item[0], item[1], item[2]) for item in liabilities if item[2] != int(remove_id)]
                
                print("\n---Tämänhetkinen BUDJETTI---\n")
                [print(printable_budget_by_group(group, item)) for (group, item) in [("Tulot", revenues), ("Menot", expenses), ("Varat", assets), ("Velat", liabilities)]]
                print("Nettotulot:", calculate_net(revenues, expenses))
                print("Nettovarat:", calculate_net(assets, liabilities) + "\n")

        elif cmd == "4":
            run_login_ui(db)
