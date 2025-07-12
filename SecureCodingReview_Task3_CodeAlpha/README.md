# 🔐 Secure Coding Review – Task 3 (CodeAlpha Internship)

## 📌 Task Title:
Secure Coding Review - Python GUI Login System

## 🧪 What Was Reviewed:
A Python GUI application simulating a user login/signup system using an SQLite database. The application was reviewed and upgraded with secure coding techniques such as salted password hashing and parameterized SQL queries.

## ⚠️ Issues That Were Fixed from Basic Version:
1. SQL Injection: Replaced direct query strings with parameterized queries.
2. Plaintext Passwords: Replaced with SHA-256 password hashing.
3. Predictable Hashing: Added salt to make hashes unique and resistant to dictionary attacks.
4. Password Visibility: Password input is hidden in the GUI.
5. No GUI: Replaced terminal code with a user-friendly window interface using Tkinter.

## 🔐 Fixes Applied:
- Used parameterized SQL queries to prevent SQL injection.
- Stored passwords securely using salted SHA-256 hashing.
- GUI login/signup form built with Tkinter.
- Input validation added for username and password length.

## 📁 Files:
- `secure_gui_app.py`: Final secure GUI login/signup application
- `users.db`: SQLite database created on first run
- `README.md`: This report

## 🏁 How to Run:
1. Install Python (https://www.python.org)
2. Run the file with:
```bash
python secure_gui_app.py
```

## 💡 Conclusion:
The final version is a secure and user-friendly Python login system. It demonstrates understanding of secure coding practices including hashing, input validation, and GUI application building.
