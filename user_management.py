import sqlite3

def signup_user(name, email, password):
    conn = sqlite3.connect('naming_app.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute('INSERT INTO Users (name, email, password) VALUES (?, ?, ?)', (name, email, password))
        conn.commit()
        return True
    except sqlite3.Error:
        conn.rollback()
        return False
    finally:
        conn.close()
        
def login_user(email, password):
    conn = sqlite3.connect('naming_app.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute('SELECT * FROM Users WHERE email = ? AND password = ?', (email, password))
        user = cursor.fetchone()
        if user:
            return user
        else:
            return None
    except sqlite3.Error:
        return None
    finally:
        conn.close()