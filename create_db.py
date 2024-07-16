import sqlite3

# Connect to SQLite database (it will create the database if it does not exist)
conn = sqlite3.connect('users.db')

# Create a cursor object
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    username TEXT PRIMARY KEY,
                    password TEXT NOT NULL)''')

# Insert sample data
cursor.execute("INSERT INTO users (username, password) VALUES ('user1', 'password1')")
cursor.execute("INSERT INTO users (username, password) VALUES ('user2', 'password2')")

# Commit the changes and close the connection
conn.commit()
conn.close()
