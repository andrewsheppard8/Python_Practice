from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"  # needed for flash messages

DB_PATH = os.path.join(os.getcwd(), "users.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)
    conn.commit()
    conn.close()

# --- Password validation logic (from your standalone script) ---
def validate_password(password, length):
    errors = []

    if len(password) != length:
        errors.append(f"Password must be exactly {length} characters long.")
    
    if not any(i.isupper() for i in password):
        errors.append("Password must contain at least one uppercase letter.")
    if not any(i.islower() for i in password):
        errors.append("Password must contain at least one lowercase letter.")
    if not any(i.isdigit() for i in password):
        errors.append("Password must contain at least one number.")
    if not any(not i.isalnum() for i in password):
        errors.append("Password must contain at least one special character.")

    return errors  # empty list means password is valid

@app.route("/")
def home():
    return redirect(url_for("register"))

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        pass_length = int(request.form.get("pass_length", 8))  # default 8

        # --- Step 1: Check if username exists ---
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username = ?", (username,))
        if c.fetchone():
            conn.close()
            flash("Username already exists.", "error")
            return redirect(url_for("register"))

        # --- Step 2: Check password validity ---
        errors = validate_password(password, pass_length)
        if errors:
            for err in errors:
                flash(err, "error")
            conn.close()
            return redirect(url_for("register"))

        # --- Step 3: Insert new user ---
        try:
            c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            flash("Account created successfully!", "success")
        finally:
            conn.close()

        return redirect(url_for("register"))

    return render_template("register.html")

@app.route("/delete_user", methods=["GET", "POST"])
def delete_user():
    if request.method == "POST":
        username = request.form["username"]

        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()

        # Check if user exists
        c.execute("SELECT * FROM users WHERE username = ?", (username,))
        if c.fetchone():
            c.execute("DELETE FROM users WHERE username = ?", (username,))
            conn.commit()
            flash(f"User '{username}' deleted successfully!", "success")
        else:
            flash(f"User '{username}' does not exist.", "error")

        conn.close()
        return redirect(url_for("delete_user"))

    return render_template("delete_user.html")

if __name__ == "__main__":
    init_db()
    app.run(debug=True)