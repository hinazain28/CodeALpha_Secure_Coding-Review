import tkinter as tk
from tkinter import messagebox
import sqlite3
import hashlib
import os

# ---------------- Database Setup ----------------
def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT UNIQUE,
            password TEXT,
            salt TEXT
        )
    ''')
    conn.commit()
    conn.close()

# ---------------- Auto Add Demo User ----------------
def add_demo_user():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    count = cursor.fetchone()[0]

    if count == 0:
        username = "admin"
        password = "admin123"
        salt = os.urandom(16).hex()
        hashed = hashlib.sha256((password + salt).encode()).hexdigest()
        cursor.execute("INSERT INTO users (username, password, salt) VALUES (?, ?, ?)", (username, hashed, salt))
        conn.commit()
        print("✅ Demo user added: admin / admin123")
    conn.close()

# ---------------- Hashing ----------------
def hash_password(password, salt=None):
    if salt is None:
        salt = os.urandom(16).hex()
    hashed = hashlib.sha256((password + salt).encode()).hexdigest()
    return hashed, salt

def verify_password(stored_hash, salt, input_password):
    return stored_hash == hashlib.sha256((input_password + salt).encode()).hexdigest()

# ---------------- Logic ----------------
def signup():
    username = entry_username.get()
    password = entry_password.get()

    if len(username) < 3 or len(password) < 4:
        messagebox.showerror("Error", "Username or password too short!")
        return

    hashed_pw, salt = hash_password(password)

    try:
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password, salt) VALUES (?, ?, ?)",
                       (username, hashed_pw, salt))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "User registered successfully!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Username already exists!")

def login():
    username = entry_username.get()
    password = entry_password.get()

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT password, salt FROM users WHERE username = ?", (username,))
    record = cursor.fetchone()
    conn.close()

    if record:
        stored_hash, salt = record
        if verify_password(stored_hash, salt, password):
            messagebox.showinfo("Login", "✅ Login Successful!")
        else:
            messagebox.showerror("Login", "❌ Incorrect Password!")
    else:
        messagebox.showerror("Login", "❌ User Not Found!")

# ---------------- GUI Setup ----------------
init_db()
add_demo_user()

# Main Window
window = tk.Tk()
window.title("Secure Login System")
window.geometry("400x350")
window.config(bg="#f0f0f0")
window.resizable(False, False)

# Title
title_label = tk.Label(window, text="🔐 Secure Login System", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
title_label.pack(pady=20)

# Form Frame
form_frame = tk.Frame(window, bg="#ffffff", bd=2, relief="groove", padx=20, pady=20)
form_frame.pack(pady=10)

# Username
tk.Label(form_frame, text="Username:", font=("Arial", 12), bg="#ffffff").grid(row=0, column=0, sticky="e", pady=5)
entry_username = tk.Entry(form_frame, width=30, font=("Arial", 11))
entry_username.grid(row=0, column=1, pady=5)

# Password
tk.Label(form_frame, text="Password:", font=("Arial", 12), bg="#ffffff").grid(row=1, column=0, sticky="e", pady=5)
entry_password = tk.Entry(form_frame, show="*", width=30, font=("Arial", 11))
entry_password.grid(row=1, column=1, pady=5)

# Buttons
btn_frame = tk.Frame(window, bg="#f0f0f0")
btn_frame.pack(pady=10)

btn_signup = tk.Button(btn_frame, text="Sign Up", command=signup, width=12, bg="#4CAF50", fg="white", font=("Arial", 11))
btn_signup.grid(row=0, column=0, padx=10)

btn_login = tk.Button(btn_frame, text="Login", command=login, width=12, bg="#2196F3", fg="white", font=("Arial", 11))
btn_login.grid(row=0, column=1, padx=10)

# Footer
tk.Label(window, text="Demo User: admin / admin123", font=("Arial", 9), bg="#f0f0f0", fg="gray").pack(side="bottom", pady=5)

window.mainloop()
