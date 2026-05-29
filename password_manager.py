from tkinter import *
from tkinter import messagebox
from cryptography.fernet import Fernet
import os
import random
import string

# Create or Load Secret Key
def load_key():
    if not os.path.exists("secret.key"):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as file:
            file.write(key)
    else:
        with open("secret.key", "rb") as file:
            key = file.read()
    return key

key = load_key()
fernet = Fernet(key)

# Save Password
def save_password():

    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if website == "" or username == "" or password == "":
        messagebox.showerror("Error", "Fill all fields")
        return

    encrypted_password = fernet.encrypt(password.encode())

    with open("passwords.txt", "ab") as file:
        data = f"{website} | {username} | ".encode()
        file.write(data + encrypted_password + b"\n")

    messagebox.showinfo("Success", "Password Saved")

    website_entry.delete(0, END)
    username_entry.delete(0, END)
    password_entry.delete(0, END)

# View Passwords
def view_passwords():

    if not os.path.exists("passwords.txt"):
        messagebox.showinfo("Info", "No passwords found")
        return

    top = Toplevel(root)
    top.title("Saved Passwords")
    top.geometry("600x400")

    text_area = Text(top, font=("Arial", 12))
    text_area.pack(fill=BOTH, expand=True)

    with open("passwords.txt", "rb") as file:

        lines = file.readlines()

        for line in lines:

            parts = line.strip().split(b" | ")

            if len(parts) == 3:

                website = parts[0].decode()
                username = parts[1].decode()
                encrypted_password = parts[2]

                try:
                    decrypted_password = fernet.decrypt(encrypted_password).decode()
                except:
                    decrypted_password = "Error"

                text_area.insert(END, f"Website : {website}\n")
                text_area.insert(END, f"Username : {username}\n")
                text_area.insert(END, f"Password : {decrypted_password}\n")
                text_area.insert(END, "-" * 40 + "\n")

# Generate Password
def generate_password():

    characters = string.ascii_letters + string.digits + "@#$%&*"

    generated = "".join(random.choice(characters) for i in range(12))

    password_entry.delete(0, END)
    password_entry.insert(0, generated)

# Main Window
root = Tk()
root.title("Password Manager")
root.geometry("500x500")
root.config(bg="#2c3e50")

# Heading
Label(
    root,
    text="Password Manager",
    font=("Arial", 24, "bold"),
    bg="#2c3e50",
    fg="white"
).pack(pady=20)

# Website
Label(
    root,
    text="Website",
    font=("Arial", 14),
    bg="#2c3e50",
    fg="white"
).pack()

website_entry = Entry(root, font=("Arial", 14), width=30)
website_entry.pack(pady=5)

# Username
Label(
    root,
    text="Username / Email",
    font=("Arial", 14),
    bg="#2c3e50",
    fg="white"
).pack()

username_entry = Entry(root, font=("Arial", 14), width=30)
username_entry.pack(pady=5)

# Password
Label(
    root,
    text="Password",
    font=("Arial", 14),
    bg="#2c3e50",
    fg="white"
).pack()

password_entry = Entry(root, font=("Arial", 14), width=30, show="*")
password_entry.pack(pady=5)

# Buttons
Button(
    root,
    text="Save Password",
    font=("Arial", 12, "bold"),
    bg="green",
    fg="white",
    width=20,
    command=save_password
).pack(pady=10)

Button(
    root,
    text="View Passwords",
    font=("Arial", 12, "bold"),
    bg="blue",
    fg="white",
    width=20,
    command=view_passwords
).pack(pady=10)

Button(
    root,
    text="Generate Password",
    font=("Arial", 12, "bold"),
    bg="purple",
    fg="white",
    width=20,
    command=generate_password
).pack(pady=10)

Button(
    root,
    text="Exit",
    font=("Arial", 12, "bold"),
    bg="red",
    fg="white",
    width=20,
    command=root.quit
).pack(pady=10)

root.mainloop()