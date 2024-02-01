import string
import secrets
import tkinter as tk
from tkinter import ttk

def generate_password(length):
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation
    all_characters = uppercase_letters + lowercase_letters + digits + symbols
    password = ''.join(secrets.choice(all_characters) for _ in range(length))
    return password

def generate_password_button_clicked():
    length = int(length_entry.get())
    password = generate_password(length)
    password_label.config(text="Generated password: " + password)
root = tk.Tk()
root.title("Password Generator")
length_label = ttk.Label(root, text="Enter the length of password:")
length_label.grid(row=0, column=0, padx=10, pady=10, sticky="E")

length_entry = ttk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)

generate_button = ttk.Button(root, text="Generate Password", command=generate_password_button_clicked)
generate_button.grid(row=1, column=0, columnspan=2, pady=10)

password_label = ttk.Label(root, text="Generated password:")
password_label.grid(row=2, column=0, columnspan=2, pady=10)
root.mainloop()
