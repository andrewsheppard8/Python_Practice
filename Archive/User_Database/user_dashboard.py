from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"

DB_PATH = os.path.join(os.getcwd(), "users.db")

# --- Initialize DB ---
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

# --- Password validation logic ---
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

    return errors

# --- Routes ---

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        pass_length = int(request.form.get("pass_length", 8))

        # Check if username exists
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username = ?", (username,))
        if c.fetchone():
            flash("Username already exists.", "error")
            conn.close()
            return redirect(url_for("register"))

        # Validate password
        errors = validate_password(password, pass_length)
        if errors:
            for err in errors:
                flash(err, "error")
            conn.close()
            return redirect(url_for("register"))

        # Insert user
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()
        flash("Account created successfully!", "success")
        return redirect(url_for("register"))

    return render_template("register.html")

@app.route("/delete_user", methods=["GET", "POST"])
def delete_user():
    if request.method == "POST":
        username = request.form["username"]
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
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

@app.route("/list_users")
def list_users():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT id, username, password FROM users")
    users = c.fetchall()
    conn.close()
    return render_template("list_users.html", users=users)

# --- Run App ---
if __name__ == "__main__":
    init_db()
    app.run(debug=True)