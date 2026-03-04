import sqlite3

def get_user_data(username):
    # DANGER: SQL Injection vulnerability here!
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    
    return cursor.fetchall()

# DANGER: Hardcoded password
DB_PASSWORD = "super_secret_admin_password_123!"
