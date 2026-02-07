import hashlib
from datetime import datetime, timedelta

users = {
    "manager": {
        "username": "manager",
        "password_hash": hashlib.sha256("Manager123!".encode()).hexdigest(),
        "role": "manager",
        "failed_attempts": 0,
        "lock_until": None
    }
}

current_user = None

def hash_pw(pw):
    return hashlib.sha256(pw.encode()).hexdigest()

def register():
    global users
    print("\n=== REGISTER ===")
    username = input("Username: ").strip()
    if username in users:
        print("Username already exists.")
        return

    pw = input("Password: ")
    confirm = input("Confirm: ")

    if pw != confirm:
        print("Passwords do not match.")
        return

    users[username] = {
        "username": username,
        "password_hash": hash_pw(pw),
        "role": "customer",
        "failed_attempts": 0,
        "lock_until": None
    }

    print("Account created.")

def login():
    global current_user
    print("\n=== LOGIN ===")
    username = input("Username: ").strip()
    pw = input("Password: ")

    if username not in users:
        print("Invalid credentials.")
        return

    user = users[username]

    if user["lock_until"] and datetime.now() < user["lock_until"]:
        print("Account locked. Try later.")
        return

    if user["password_hash"] == hash_pw(pw):
        user["failed_attempts"] = 0
        user["lock_until"] = None
        current_user = user
        print(f"Welcome, {username}.")
    else:
        user["failed_attempts"] += 1
        print("Invalid credentials.")
        if user["failed_attempts"] >= 5:
            user["lock_until"] = datetime.now() + timedelta(minutes=5)
            print("Too many attempts. Locked for 5 minutes.")

def logout():
    global current_user
    current_user = None
    print("Logged out.")