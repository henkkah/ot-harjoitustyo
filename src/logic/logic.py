def print_current_budget(revenues, expenses, assets, liabilities):
    print("---Tämänhetkinen BUDJETTI---\n")
    print("TULOT:")
    revenues = sorted(revenues, key=lambda x: x[1], reverse=True) # Sorts items from highest budget item to lowest budget item
    [print( item[0] + max(1, (20 - len(item[0])))*" " + str(item[1]) ) for item in revenues]
    print()
    print("MENOT:")
    expenses = sorted(expenses, key=lambda x: x[1], reverse=True) # Sorts items from highest budget item to lowest budget item
    [print( item[0] + max(1, (20 - len(item[0])))*" " + str(item[1]) ) for item in expenses]
    print()
    print("VARAT:")
    assets = sorted(assets, key=lambda x: x[1], reverse=True) # Sorts items from highest budget item to lowest budget item
    [print( item[0] + max(1, (20 - len(item[0])))*" " + str(item[1]) ) for item in assets]
    print()
    print("VELAT:")
    liabilities = sorted(liabilities, key=lambda x: x[1], reverse=True) # Sorts items from highest budget item to lowest budget item
    [print( item[0] + max(1, (20 - len(item[0])))*" " + str(item[1]) ) for item in liabilities]
    print()

def print_current_budget_with_ids(revenues, expenses, assets, liabilities):
    print("---Budjettirivit ja id:t---\n")
    print("TULOT:")
    revenues = sorted(revenues, key=lambda x: x[1], reverse=True) # Sorts items from highest budget item to lowest budget item
    [print( item[0] + max(1, (20 - len(item[0])))*" " + str(item[1]) + " (id: " + str(item[2]) + ")" ) for item in revenues]
    print()
    print("MENOT:")
    expenses = sorted(expenses, key=lambda x: x[1], reverse=True) # Sorts items from highest budget item to lowest budget item
    [print( item[0] + max(1, (20 - len(item[0])))*" " + str(item[1]) + " (id: " + str(item[2]) + ")" ) for item in expenses]
    print()
    print("VARAT:")
    assets = sorted(assets, key=lambda x: x[1], reverse=True) # Sorts items from highest budget item to lowest budget item
    [print( item[0] + max(1, (20 - len(item[0])))*" " + str(item[1]) + " (id: " + str(item[2]) + ")" ) for item in assets]
    print()
    print("VELAT:")
    liabilities = sorted(liabilities, key=lambda x: x[1], reverse=True) # Sorts items from highest budget item to lowest budget item
    [print( item[0] + max(1, (20 - len(item[0])))*" " + str(item[1]) + " (id: " + str(item[2]) + ")" ) for item in liabilities]
    print()
