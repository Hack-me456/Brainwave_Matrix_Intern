import tkinter as tk
from tkinter import messagebox, simpledialog
import sqlite3

# Connect to DB
db_path = "inventory_system.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

try:
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("admin", "admin123"))
except sqlite3.IntegrityError:
    pass

# --------- Helper Functions --------- #
def login(username, password):
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    return cursor.fetchone() is not None

def fetch_inventory():
    cursor.execute("SELECT * FROM inventory")
    return cursor.fetchall()

def add_product(name, quantity, price):
    cursor.execute("INSERT INTO inventory (product_name, quantity, price) VALUES (?, ?, ?)", (name, quantity, price))
    conn.commit()

def delete_product(product_id):
    cursor.execute("DELETE FROM inventory WHERE id=?", (product_id,))
    conn.commit()

def update_product(product_id, quantity, price):
    cursor.execute("UPDATE inventory SET quantity=?, price=? WHERE id=?", (quantity, price, product_id))
    conn.commit()

# --------- GUI Functions --------- #
def show_inventory():
    inventory_list.delete(0, tk.END)
    for item in fetch_inventory():
        inventory_list.insert(tk.END, f"ID:{item[0]} | {item[1]} | Qty: {item[2]} | ₹{item[3]}")

def add_item():
    name = simpledialog.askstring("Product Name", "Enter product name:")
    qty = simpledialog.askinteger("Quantity", "Enter quantity:")
    price = simpledialog.askfloat("Price", "Enter price:")
    if name and qty is not None and price is not None:
        add_product(name, qty, price)
        show_inventory()

def delete_item():
    selected = inventory_list.curselection()
    if selected:
        item_text = inventory_list.get(selected[0])
        product_id = int(item_text.split('|')[0].split(':')[1])
        delete_product(product_id)
        show_inventory()

def edit_item():
    selected = inventory_list.curselection()
    if selected:
        item_text = inventory_list.get(selected[0])
        product_id = int(item_text.split('|')[0].split(':')[1])
        qty = simpledialog.askinteger("New Quantity", "Enter new quantity:")
        price = simpledialog.askfloat("New Price", "Enter new price:")
        if qty is not None and price is not None:
            update_product(product_id, qty, price)
            show_inventory()

# --------- Main Windows --------- #
def open_inventory():
    login_win.destroy()
    
    global inventory_list
    inv_win = tk.Tk()
    inv_win.title("Inventory System")

    tk.Label(inv_win, text="Inventory Items", font=("Arial", 14)).pack()
    inventory_list = tk.Listbox(inv_win, width=60)
    inventory_list.pack(pady=10)

    tk.Button(inv_win, text="Add Item", command=add_item).pack(side=tk.LEFT, padx=10)
    tk.Button(inv_win, text="Edit Item", command=edit_item).pack(side=tk.LEFT, padx=10)
    tk.Button(inv_win, text="Delete Item", command=delete_item).pack(side=tk.LEFT, padx=10)

    show_inventory()
    inv_win.mainloop()

def try_login():
    username = user_entry.get()
    password = pass_entry.get()
    if login(username, password):
        open_inventory()
    else:
        messagebox.showerror("Login Failed", "Invalid credentials!")

login_win = tk.Tk()
login_win.title("Login")

tk.Label(login_win, text="Username").pack()
user_entry = tk.Entry(login_win)
user_entry.pack()

tk.Label(login_win, text="Password").pack()
pass_entry = tk.Entry(login_win, show="*")
pass_entry.pack()

tk.Button(login_win, text="Login", command=try_login).pack(pady=10)
login_win.mainloop()
