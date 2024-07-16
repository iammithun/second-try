#!/usr/bin/env python3

import cgi
import sqlite3

# Get form data
form = cgi.FieldStorage()
username = form.getvalue('username')
password = form.getvalue('password')

# Connect to SQLite database
conn = sqlite3.connect('/path/to/your/directory/users.db')  # Update path accordingly
cursor = conn.cursor()

# Check if the user exists and the password is correct
cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
user = cursor.fetchone()

# Generate HTML response
print("Content-type: text/html\n")
if user:
    with open('/path/to/your/directory/success.html', 'r') as file:  # Update path accordingly
        print(file.read())
else:
    with open('/path/to/your/directory/error.html', 'r') as file:  # Update path accordingly
        print(file.read())

# Close the connection
conn.close()
