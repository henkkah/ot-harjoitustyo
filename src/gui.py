from tkinter import *
import tkinter.messagebox
import tkinter.simpledialog
from tkinter import ttk
from logic import handle_existing_user
from db import search_for_username
from logic import handle_new_user
from db import get_username_of_userid
from db import get_budgets_by_group
from logic import sort_budget_items_by_amount
from logic import add_new_budget_row
from logic import delete_existing_budget_row

def run_login_ui(db):
    root = Tk()
    
    bg_color = 'medium spring green'
    button_color = 'light cyan'

    root.title("BudjetointiSovellus")
    window_icon = PhotoImage(file="photos/euro_icon.png")
    root.iconphoto(False, window_icon)
    
    main_frame = Frame(root, bg=bg_color)
    main_frame.pack(expand=TRUE)
    
    second_frame = Frame(main_frame, bg=bg_color)
    second_frame.grid(padx=50, pady=50)

    username_label = Label(second_frame, text="Käyttäjätunnus:", bg=bg_color)
    password_label = Label(second_frame, text="Salasana:", bg=bg_color)
    username_entry = Entry(second_frame)
    password_entry = Entry(second_frame)
    password_entry.config(show="*")

    username_label.grid(row=0, column=0, sticky=E, pady=2)
    password_label.grid(row=1, column=0, sticky=E, pady=2)
    username_entry.grid(row=0, column=1, pady=2)
    password_entry.grid(row=1, column=1, pady=2)

    def authenticate(event):
        success, userid, error = handle_existing_user(db, username_entry.get(), password_entry.get())
        if not success:
            tkinter.messagebox.showinfo("Virhe", error)
        else:
            root.destroy()
            run_budget_ui(db, userid)

    def create_new_user(event):
        root.destroy()
        new_root = Tk()
        
        new_root.title("BudjetointiSovellus")

        main_frame = Frame(new_root, bg=bg_color)
        main_frame.pack(expand=TRUE)
        
        second_frame = Frame(main_frame, bg=bg_color)
        second_frame.grid(padx=25, pady=25)
        
        username_label = Label(second_frame, text="Käyttäjätunnus:", bg=bg_color)
        password_label_1 = Label(second_frame, text="Salasana:", bg=bg_color)
        password_label_2 = Label(second_frame, text="Toista Salasana:", bg=bg_color)
        username_entry = Entry(second_frame)
        password_entry_1 = Entry(second_frame)
        password_entry_2 = Entry(second_frame)
        password_entry_1.config(show="*")
        password_entry_2.config(show="*")

        username_label.grid(row=0, column=0, sticky=E, pady=2)
        password_label_1.grid(row=1, column=0, sticky=E, pady=2)
        password_label_2.grid(row=2, column=0, sticky=E, pady=2)
        username_entry.grid(row=0, column=1, pady=2)
        password_entry_1.grid(row=1, column=1, pady=2)
        password_entry_2.grid(row=2, column=1, pady=2)
        
        def create_user_with_input(event):
            given_username = username_entry.get()
            given_password_1 = password_entry_1.get()
            given_password_2 = password_entry_2.get()
            try:
                if search_for_username(db, given_username) == given_username:
                    tkinter.messagebox.showinfo("Virhe", "Käyttäjätunnus on jo käytössä!")
                    return
            except:
                if given_username == "":
                    tkinter.messagebox.showinfo("Virhe", "Anna Käyttäjätunnus!")
                    return
                elif given_password_1 != given_password_2:
                    tkinter.messagebox.showinfo("Virhe", "Salasanat eivät täsmää!")
                    return
            
            if given_username is not None:
                success, userid, error = handle_new_user(db, given_username, given_password_1)
                new_root.destroy()
                run_budget_ui(db, userid)
        
        create_user_button = Button(second_frame, text="Luo käyttäjä", bg=button_color)
        create_user_button.bind("<Button-1>", create_user_with_input)
        create_user_button.bind("<Return>", create_user_with_input)
        create_user_button.grid(row=3, columnspan=2, pady=2)
        
        def on_closing():
            new_root.destroy()
            run_login_ui(db)

        new_root.protocol("WM_DELETE_WINDOW", on_closing)
        
        new_root.mainloop()

    def close_app(event):
        exit()

    login_button = Button(second_frame, text="Kirjaudu sisään", bg=button_color)
    login_button.bind("<Button-1>", authenticate)
    login_button.bind("<Return>", authenticate)
    login_button.grid(row=2, columnspan=2, pady=2)

    empty_canvas = Canvas(second_frame, height=25, width=0, bg=bg_color, highlightthickness=0)
    empty_canvas.grid(row=3, columnspan=2, pady=2)

    create_new_user_button = Button(second_frame, text="Luo uusi käyttäjä", bg=button_color)
    create_new_user_button.bind("<Button-1>", create_new_user)
    create_new_user_button.bind("<Return>", create_new_user)
    create_new_user_button.grid(row=4, columnspan=2, pady=2)
    
    close_app_button = Button(second_frame, text="Sulje sovellus", bg=button_color)
    close_app_button.bind("<Button-1>", close_app)
    close_app_button.bind("<Return>", close_app)
    close_app_button.grid(row=5, columnspan=2, pady=2)

    root.mainloop()

####################################################################################################

def run_budget_ui(db, userid):
    root = Tk()
    
    bg_color = 'medium spring green'
    button_color = 'light cyan'

    root.title("BudjetointiSovellus")
    window_icon = PhotoImage(file="photos/euro_icon.png")
    root.iconphoto(False, window_icon)

    main_frame = Frame(root, bg=bg_color)
    main_frame.pack(expand=TRUE)

    top_frame = Frame(main_frame, bg=bg_color)
    middle_frame = Frame(main_frame, bg=bg_color)
    bottom_frame = Frame(main_frame, bg=bg_color)

    top_frame.grid(columnspan=4, padx=25, pady=25)
    middle_frame.grid(columnspan=4, padx=25, pady=25)
    bottom_frame.grid(columnspan=4, padx=25, pady=25)
    
    def logout(event):
        root.destroy()
        run_login_ui(db)
    
    username_label = Label(top_frame, text=get_username_of_userid(db, userid), bg=bg_color)
    username_label.pack(side=LEFT)
    logout_button = Button(top_frame, text="Kirjaudu ulos", bg=button_color)
    logout_button.bind("<Button-1>", logout)
    logout_button.bind("<Return>", logout)
    logout_button.pack(side=RIGHT)

    expenses_frame = Frame(middle_frame, bg=bg_color)
    revenues_frame = Frame(middle_frame, bg=bg_color)
    assets_frame = Frame(middle_frame, bg=bg_color)
    liabilities_frame = Frame(middle_frame, bg=bg_color)
    summary_frame = Frame(middle_frame, bg=bg_color)
    
    expenses_frame.grid(row=0, column=0, padx=20, pady=10, sticky=NW)
    revenues_frame.grid(row=0, column=1, padx=20, pady=10, sticky=NW)
    assets_frame.grid(row=1, column=0, padx=20, pady=10, sticky=NW)
    liabilities_frame.grid(row=1, column=1, padx=20, pady=10, sticky=NW)
    summary_frame.grid(row=2, columnspan=3, padx=20, pady=10)
    
    expenses_label = Label(expenses_frame, text="Menot", font="bold", bg=bg_color)
    revenues_label = Label(revenues_frame, text="Tulot", font="bold", bg=bg_color)
    assets_label = Label(assets_frame, text="Varat", font="bold", bg=bg_color)
    liabilities_label = Label(liabilities_frame, text="Velat", font="bold", bg=bg_color)
    
    expenses_content = Frame(expenses_frame, bg=bg_color)
    revenues_content = Frame(revenues_frame, bg=bg_color)
    assets_content = Frame(assets_frame, bg=bg_color)
    liabilities_content = Frame(liabilities_frame, bg=bg_color)

    expenses_label.grid(row=0, sticky=W)
    revenues_label.grid(row=0, sticky=W)
    assets_label.grid(row=0, sticky=W)
    liabilities_label.grid(row=0, sticky=W)
    
    expenses_content.grid(row=1, columnspan=2, sticky=NW)
    revenues_content.grid(row=1, columnspan=2, sticky=NW)
    assets_content.grid(row=1, columnspan=2, sticky=NW)
    liabilities_content.grid(row=1, columnspan=2, sticky=NW)
    
    revenues, expenses, assets, liabilities = get_budgets_by_group(db, userid)
    revenues = sort_budget_items_by_amount(revenues)
    expenses = sort_budget_items_by_amount(expenses)
    assets = sort_budget_items_by_amount(assets)
    liabilities = sort_budget_items_by_amount(liabilities)
    
    # Expense amounts
    total_expenses = 0
    n = len(expenses)
    for i in range(n):
        name = expenses[i][0]
        amount = expenses[i][1]
        total_expenses += int(amount)
        name_label = Label(expenses_content, text=name, bg=bg_color)
        
        amount_str = str(amount)
        division = len(amount_str) % 3
        amount_ = ""
        for j in range(len(amount_str)):
            if j % 3 == division:
                amount_ += " "
            amount_ += amount_str[j]
        
        amount_label = Label(expenses_content, text=amount_, bg=bg_color)
        name_label.grid(row=i, sticky=W)
        amount_label.grid(row=i, column=1, sticky=E)
    canv1 = Canvas(expenses_content, height=1, width=1, bg=bg_color, highlightthickness=0)
    
    total_expenses_str = str(total_expenses)
    division = len(total_expenses_str) % 3
    total__expenses = ""
    for i in range(len(total_expenses_str)):
        if i % 3 == division:
            total__expenses += " "
        total__expenses += total_expenses_str[i]
    
    total_amount_label = Label(expenses_content, text=str(total__expenses), borderwidth=2, relief="groove", bg=bg_color)
    canv1.grid(row=n, sticky=W)
    total_amount_label.grid(row=n, column=1, sticky=E)
    
    # Revenue amounts
    total_revenues = 0
    n = len(revenues)
    for i in range(n):
        name = revenues[i][0]
        amount = revenues[i][1]
        total_revenues += int(amount)
        name_label = Label(revenues_content, text=name, bg=bg_color)
        
        amount_str = str(amount)
        division = len(amount_str) % 3
        amount_ = ""
        for j in range(len(amount_str)):
            if j % 3 == division:
                amount_ += " "
            amount_ += amount_str[j]
        
        amount_label = Label(revenues_content, text=amount_, bg=bg_color)
        name_label.grid(row=i, sticky=W)
        amount_label.grid(row=i, column=1, sticky=E)
    canv2 = Canvas(revenues_content, height=1, width=1, bg=bg_color, highlightthickness=0)
    
    total_revenues_str = str(total_revenues)
    division = len(total_revenues_str) % 3
    total__revenues = ""
    for i in range(len(total_revenues_str)):
        if i % 3 == division:
            total__revenues += " "
        total__revenues += total_revenues_str[i]
    
    total_amount_label = Label(revenues_content, text=str(total__revenues), borderwidth=2, relief="groove", bg=bg_color)
    canv2.grid(row=n, sticky=W)
    total_amount_label.grid(row=n, column=1, sticky=E)
    
    # Asset amounts
    total_assets = 0
    n = len(assets)
    for i in range(n):
        name = assets[i][0]
        amount = assets[i][1]
        total_assets += int(amount)
        name_label = Label(assets_content, text=name, bg=bg_color)
        
        amount_str = str(amount)
        division = len(amount_str) % 3
        amount_ = ""
        for j in range(len(amount_str)):
            if j % 3 == division:
                amount_ += " "
            amount_ += amount_str[j]
        
        amount_label = Label(assets_content, text=amount_, bg=bg_color)
        name_label.grid(row=i, sticky=W)
        amount_label.grid(row=i, column=1, sticky=E)
    canv3 = Canvas(assets_content, height=1, width=1, bg=bg_color, highlightthickness=0)
    
    total_assets_str = str(total_assets)
    division = len(total_assets_str) % 3
    total__assets = ""
    for i in range(len(total_assets_str)):
        if i % 3 == division:
            total__assets += " "
        total__assets += total_assets_str[i]
    
    total_amount_label = Label(assets_content, text=str(total__assets), borderwidth=2, relief="groove", bg=bg_color)
    canv3.grid(row=n, sticky=W)
    total_amount_label.grid(row=n, column=1, sticky=E)
    
    # Liability amounts
    total_liabilities = 0
    n = len(liabilities)
    for i in range(n):
        name = liabilities[i][0]
        amount = liabilities[i][1]
        total_liabilities += int(amount)
        name_label = Label(liabilities_content, text=name, bg=bg_color)
        
        amount_str = str(amount)
        division = len(amount_str) % 3
        amount_ = ""
        for j in range(len(amount_str)):
            if j % 3 == division:
                amount_ += " "
            amount_ += amount_str[j]
        
        amount_label = Label(liabilities_content, text=amount_, bg=bg_color)
        name_label.grid(row=i, sticky=W)
        amount_label.grid(row=i, column=1, sticky=E)
    canv4 = Canvas(assets_content, height=1, width=1, bg=bg_color, highlightthickness=0)
    
    total_liabilities_str = str(total_liabilities)
    division = len(total_liabilities_str) % 3
    total__liabilities = ""
    for i in range(len(total_liabilities_str)):
        if i % 3 == division:
            total__liabilities += " "
        total__liabilities += total_liabilities_str[i]
    
    total_amount_label = Label(liabilities_content, text=str(total__liabilities), borderwidth=2, relief="groove", bg=bg_color)
    canv4.grid(row=n, sticky=W)
    total_amount_label.grid(row=n, column=1, sticky=E)
    
    net_assets_frame = Frame(summary_frame, bg=bg_color)
    mid_label = Label(summary_frame, text="-", bg=bg_color)
    net_revenues_frame = Frame(summary_frame, bg=bg_color)
    net_assets_frame.grid(row=0, column=0)
    mid_label.grid(row=0, column=1)
    net_revenues_frame.grid(row=0, column=2)
    
    net_assets = total_assets - total_liabilities
    net_revenues = total_revenues - total_expenses
    
    net_assets_str = str(net_assets)
    division = len(net_assets_str) % 3
    net__assets = ""
    for i in range(len(net_assets_str)):
        if i % 3 == division:
            net__assets += " "
        net__assets += net_assets_str[i]

    net_revenues_str = str(net_revenues)
    division = len(net_revenues_str) % 3
    net__revenues = ""
    for i in range(len(net_revenues_str)):
        if i % 3 == division:
            net__revenues += " "
        net__revenues += net_revenues_str[i]
    
    net_assets_label = Label(net_assets_frame, text="Nettovarat:", bg=bg_color)
    net_revenues_label = Label(net_revenues_frame, text="Nettotulot:", bg=bg_color)
    net_assets_amount_label = Label(net_assets_frame, text=net__assets, bg=bg_color)
    net_revenues_amount_label = Label(net_revenues_frame, text=net__revenues, bg=bg_color)
    
    net_assets_label.grid(row=0, column=0, sticky=W)
    net_assets_amount_label.grid(row=0, column=1, sticky=E)
    net_revenues_label.grid(row=0, column=0, sticky=W)
    net_revenues_amount_label.grid(row=0, column=1, sticky=E)

    def add_row(event):
        root.destroy()
        
        new_root = Tk()
        
        new_root.title("BudjetointiSovellus")

        main_frame = Frame(new_root, bg=bg_color)
        main_frame.pack(expand=TRUE)
        
        second_frame = Frame(main_frame, bg=bg_color)
        second_frame.grid(padx=25, pady=25)
        
        instruction_label = Label(second_frame, text="Lisää uusi budjettirivi:", font="bold", bg=bg_color)
        class_label = Label(second_frame, text="Valitse luokka:", bg=bg_color)
        name_label = Label(second_frame, text="Budjettirivin nimi:", bg=bg_color)
        amount_label = Label(second_frame, text="Budjettirivin summa:", bg=bg_color)
        add_row_button = Button(second_frame, text="Lisää budjettirivi", bg=button_color)
        
        n = StringVar()
        class_dropdown = ttk.Combobox(second_frame, width = 17, textvariable = n)
        class_dropdown['values'] = ('Tulot', 'Menot', 'Varat', 'Velat')
        
        name_entry = Entry(second_frame)
        amount_entry = Entry(second_frame)
        
        instruction_label.grid(row=0, columnspan=2, pady=2)
        class_label.grid(row=1, sticky=E, pady=2)
        class_dropdown.grid(row=1, column=1, sticky=W, pady=2)
        name_label.grid(row=2, sticky=E, pady=2)
        name_entry.grid(row=2, column=1, sticky=W, pady=2)
        amount_label.grid(row=3, sticky=E, pady=2)
        amount_entry.grid(row=3, column=1, sticky=W, pady=2)
        
        def add_row_with_input(event):
            classification = class_dropdown.get()
            if classification == "Tulot" or classification == "Menot" or classification == "Varat" or classification == "Velat":
                pass
            else:
                tkinter.messagebox.showinfo("Virhe", "Valitse luokaksi Tulot, Menot, Varat tai Velat!")
                return
            
            name = name_entry.get()
            if name != "":
                pass
            else:
                tkinter.messagebox.showinfo("Virhe", "Anna budjettiriville nimi!")
                return
            
            amount = amount_entry.get()
            try:
                amount = int(amount)
            except:
                tkinter.messagebox.showinfo("Virhe", "Anna budjettiriville summa kokonaislukuna!")
                return
        
            success, classification, name, amount, budget_id = add_new_budget_row(db, userid, classification, name, amount)
            
            if success:
                tkinter.messagebox.showinfo("BudjetointiSovellus", "Uusi budjettirivi lisätty!")
                new_root.destroy()
                run_budget_ui(db, userid)
        
        add_row_button.bind("<Button-1>", add_row_with_input)
        add_row_button.bind("<Return>", add_row_with_input)
        add_row_button.grid(row=4, columnspan=2, pady=2)
        
        def on_closing():
            new_root.destroy()
            run_budget_ui(db, userid)

        new_root.protocol("WM_DELETE_WINDOW", on_closing)
        
        new_root.mainloop()
        
    def delete_row(event):
        root.destroy()
        
        new_root = Tk()
        
        new_root.title("BudjetointiSovellus")

        main_frame = Frame(new_root, bg=bg_color)
        main_frame.pack(expand=TRUE)

        top_frame = Frame(main_frame, bg=bg_color)
        top_frame.grid(columnspan=2, padx=25, pady=25)
        
        bottom_frame = Frame(main_frame, bg=bg_color)
        bottom_frame.grid(columnspan=3, padx=25, pady=25)
        
        expenses_frame = Frame(top_frame, bg=bg_color)
        revenues_frame = Frame(top_frame, bg=bg_color)
        assets_frame = Frame(top_frame, bg=bg_color)
        liabilities_frame = Frame(top_frame, bg=bg_color)
        
        expenses_frame.grid(row=0, column=0, padx=10, pady=10, sticky=NW)
        revenues_frame.grid(row=0, column=1, padx=10, pady=10, sticky=NW)
        assets_frame.grid(row=1, column=0, padx=10, pady=10, sticky=NW)
        liabilities_frame.grid(row=1, column=1, padx=10, pady=10, sticky=NW)
        
        expenses_label = Label(expenses_frame, text="Menot", font="bold", bg=bg_color)
        revenues_label = Label(revenues_frame, text="Tulot", font="bold", bg=bg_color)
        assets_label = Label(assets_frame, text="Varat", font="bold", bg=bg_color)
        liabilities_label = Label(liabilities_frame, text="Velat", font="bold", bg=bg_color)
        
        expenses_content = Frame(expenses_frame, bg=bg_color)
        revenues_content = Frame(revenues_frame, bg=bg_color)
        assets_content = Frame(assets_frame, bg=bg_color)
        liabilities_content = Frame(liabilities_frame, bg=bg_color)

        expenses_label.grid(row=0, sticky=W)
        revenues_label.grid(row=0, sticky=W)
        assets_label.grid(row=0, sticky=W)
        liabilities_label.grid(row=0, sticky=W)
        
        expenses_content.grid(row=1, columnspan=3, sticky=NW)
        revenues_content.grid(row=1, columnspan=3, sticky=NW)
        assets_content.grid(row=1, columnspan=3, sticky=NW)
        liabilities_content.grid(row=1, columnspan=3, sticky=NW)
        
        revenues, expenses, assets, liabilities = get_budgets_by_group(db, userid)
        revenues = sort_budget_items_by_amount(revenues)
        expenses = sort_budget_items_by_amount(expenses)
        assets = sort_budget_items_by_amount(assets)
        liabilities = sort_budget_items_by_amount(liabilities)
        
        n = len(expenses)
        for i in range(n):
            name = expenses[i][0]
            amount = expenses[i][1]
            id = expenses[i][2]
            name_label = Label(expenses_content, text=name, bg=bg_color)
            amount_label = Label(expenses_content, text=amount, bg=bg_color)
            id_label = Label(expenses_content, text="(id: " + str(id) + ")", bg=bg_color)
            name_label.grid(row=i, sticky=W)
            amount_label.grid(row=i, column=1, sticky=E)
            id_label.grid(row=i, column=2, sticky=E)
        
        n = len(revenues)
        for i in range(n):
            name = revenues[i][0]
            amount = revenues[i][1]
            id = revenues[i][2]
            name_label = Label(revenues_content, text=name, bg=bg_color)
            amount_label = Label(revenues_content, text=amount, bg=bg_color)
            id_label = Label(revenues_content, text="(id: " + str(id) + ")", bg=bg_color)
            name_label.grid(row=i, sticky=W)
            amount_label.grid(row=i, column=1, sticky=E)
            id_label.grid(row=i, column=2, sticky=E)
        
        n = len(assets)
        for i in range(n):
            name = assets[i][0]
            amount = assets[i][1]
            id = assets[i][2]
            name_label = Label(assets_content, text=name, bg=bg_color)
            amount_label = Label(assets_content, text=amount, bg=bg_color)
            id_label = Label(assets_content, text="(id: " + str(id) + ")", bg=bg_color)
            name_label.grid(row=i, sticky=W)
            amount_label.grid(row=i, column=1, sticky=E)
            id_label.grid(row=i, column=2, sticky=E)
        
        n = len(liabilities)
        for i in range(n):
            name = liabilities[i][0]
            amount = liabilities[i][1]
            id = liabilities[i][2]
            name_label = Label(liabilities_content, text=name, bg=bg_color)
            amount_label = Label(liabilities_content, text=amount, bg=bg_color)
            id_label = Label(liabilities_content, text="(id: " + str(id) + ")", bg=bg_color)
            name_label.grid(row=i, sticky=W)
            amount_label.grid(row=i, column=1, sticky=E)
            id_label.grid(row=i, column=2, sticky=E)
        
        instruction_label = Label(bottom_frame, text="Poistettavan budjettirivin id:", bg=bg_color)
        remove_entry = Entry(bottom_frame, width=10)
        remove_button = Button(bottom_frame, text="Poista", bg=button_color)

        def remove_budget_row(event):
            remove_id = remove_entry.get()
            try:
                remove_id = int(remove_id)
                success, classification, remove_id = delete_existing_budget_row(db, userid, remove_id)
            except:
                tkinter.messagebox.showinfo("Virhe", "Annoit virheellisen budjettirivin id:n!")
                return
        
            if success:
                tkinter.messagebox.showinfo("BudjetointiSovellus", "Budjettirivi poistettu!")
                new_root.destroy()
                run_budget_ui(db, userid)

        instruction_label.grid(row=0, pady=2)
        remove_entry.grid(row=0, column=1, pady=2)
        remove_button.grid(row=0, column=2, pady=2)
        remove_button.bind("<Button-1>", remove_budget_row)
        remove_button.bind("<Return>", remove_budget_row)
        
        def on_closing():
            new_root.destroy()
            run_budget_ui(db, userid)

        new_root.protocol("WM_DELETE_WINDOW", on_closing)
        
        new_root.mainloop()

    add_row_button = Button(bottom_frame, text="Lisää budjettirivi", bg=button_color)
    delete_row_button = Button(bottom_frame, text="Poista budjettirivi", bg=button_color)
    empty_canvas1 = Canvas(bottom_frame, height=5, width=5, bg=bg_color, highlightthickness=0)
    
    add_row_button.bind("<Button-1>", add_row)
    add_row_button.bind("<Return>", add_row)
    delete_row_button.bind("<Button-1>", delete_row)
    delete_row_button.bind("<Return>", delete_row)

    add_row_button.pack(side=LEFT)
    empty_canvas1.pack(side=LEFT)
    delete_row_button.pack(side=LEFT)

    root.mainloop()
