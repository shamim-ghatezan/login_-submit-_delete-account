import tkinter as tk
import json

def submit():
    username = entry_username.get()
    password = entry_password.get()

    if not username or not password:
        lbl_result.config(text="Please enter both username and password", fg="red",bg="#052659")
        return

    users = load_users()
    if username in users:
        lbl_result.config(text="This username is already submited", fg="red",bg="#052659")
    else:
        users[username] = password
        save_users(users)
        lbl_result.config(text="submit successfuly", fg="green",bg="#052659")

def login():
    username = entry_username.get()
    password = entry_password.get()

    if not username or not password:
        lbl_result.config(text="Please enter both username and password", fg="red")
        return

    users = load_users()
    if username in users and users[username] == password:
        lbl_result.config(text="Login successful", fg="green")
    else:
        lbl_result.config(text="Incorrect username or password", fg="red")

def delete_account():
    username = entry_username.get()

    if not username:
        lbl_result.config(text="Please enter the username", fg="red")
        return

    users = load_users()
    if username in users:
        del users[username]
        save_users(users)
        lbl_result.config(text="Account deleted successfully", fg="green")
    else:
        lbl_result.config(text="Username not found.", fg="red")

def load_users():
    try:
        with open("users.json", "r") as f:
            users = json.load(f)
    except FileNotFoundError:
        users = {}
    return users

def save_users(users):
    with open("users.json", "w") as f:
        json.dump(users, f)

# Create window
root = tk.Tk()
root.title("login_ submit _delete account")
root.geometry("400x250")
root.configure(bg="cyan4")

# Create widgets
label_username = tk.Label(root, text="Username:",bg="#7DA0CA")
label_username.pack()

entry_username = tk.Entry(root)
entry_username.pack()

label_password = tk.Label(root, text="Password:",bg="#7DA0CA")
label_password.pack()

entry_password = tk.Entry(root, show="*")
entry_password.pack()

lbl_result = tk.Label(root, text="", fg="black")
lbl_result.pack()

btn_submit = tk.Button(root, text="submit", command=submit,bg="#C1E8FF")
btn_submit.pack()

btn_login = tk.Button(root, text="Login", command=login,bg="#C1E8FF")
btn_login.pack()

btn_delete_account = tk.Button(root, text="Delete Account", command=delete_account,bg="#D59D80")
btn_delete_account.pack()

# Run the main loop
root.mainloop()

