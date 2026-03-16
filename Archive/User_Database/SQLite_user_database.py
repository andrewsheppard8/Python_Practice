import sqlite3

# --- Database setup ---
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
""")

# --- Username creation ---
def get_username():
    while True:
        username = input("Enter a username: ")

        # Check if username already exists
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        if cursor.fetchone():
            print("Username already exists. Please choose another.")
        else:
            return username

# --- Password creation ---
def get_password():
    while True:
        pass_length = input("Enter required password length: ")

        if pass_length.isdigit():
            pass_int = int(pass_length)
            break
        else:
            print("Please give a valid number, not a letter or symbol")

    print(f"Password must be {pass_int} characters long")

    while True:
        password = input("Enter password: ")
        pass_len = len(password)

        if pass_len < pass_int:
            print("Password not long enough")
            continue
        elif pass_len > pass_int:
            print("Password too long")
            continue

        # Validation rules
        alpha = any(i.isalpha() for i in password)
        number = any(i.isdigit() for i in password)
        special = any(not i.isalnum() for i in password)
        uppercase = any(i.isupper() for i in password)
        lowercase = any(i.islower() for i in password)

        if alpha and number and special and uppercase and lowercase:
            confirm = input("Re-enter password to confirm: ")
            if confirm == password:
                print("Password accepted")
                return password
            else:
                print("Passwords do not match. Please try again.")
                continue
        else:
            print("Password must include uppercase, lowercase, numbers, and special characters")

# --- Main account creation flow ---
def create_account():
    username = get_username()
    password = get_password()

    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    print(f"Account for '{username}' created successfully!")

# Run it
create_account()

conn.close()