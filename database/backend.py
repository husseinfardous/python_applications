# Backend of Database Application
# Imported by 'app.py'

# Import Module
import sqlite3



# Make a Database Connection and Create a Table
def connect():

    # Make a Database Connection
    connection = sqlite3.connect("books.db")

    # Make a Cursor Object in order to execute SQL statements
    cursor = connection.cursor()
    
    # Create a Table called 'book' (if it doesn't exist already) to store the ID, Title, Author, Year, and ISBN of each book
    cursor.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")

    # Commit the Changes and Close the Connection
    connection.commit()
    connection.close()



# Handle User Requests

# View All Entries
def view():

    # Connect to the Database and Makes a Cursor Object
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()

    # Retrieve All Books from the Table
    cursor.execute("SELECT * FROM book") 
    rows = cursor.fetchall()

    # Close the Connection
    connection.close()

    # Return All Books in a Tuple
    return rows

# Search for Entry
def search(title = "", author = "", year = "", isbn = ""):

    # Connect to the Database and Makes a Cursor Object
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()

    # Retrieve Book(s) that match the Query from the Table
    cursor.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ?", (title, author, year, isbn)) 
    rows = cursor.fetchall()

    # Close the Connection
    connection.close()

    # Return Book(s) in a Tuple
    return rows

# Add Entry
def add(title, author, year, isbn):

    # Connect to the Database and Makes a Cursor Object
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()

    # Insert a Book into the Table
    cursor.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn)) 

    # Commit the Changes and Close the Connection
    connection.commit()
    connection.close()

# Update Entry
def update(id, title, author, year, isbn):

    # Connect to the Database and Makes a Cursor Object
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()

    # Update a Book from the Table by ID
    cursor.execute("UPDATE book SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?", (title, author, year, isbn, id)) 

    # Commit the Changes and Close the Connection
    connection.commit()
    connection.close()

# Delete Entry
def delete(id):

    # Connect to the Database and Makes a Cursor Object
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()

    # Delete a Book from the Table by ID
    cursor.execute("DELETE FROM book WHERE id = ?", (id,)) 

    # Commit the Changes and Close the Connection
    connection.commit()
    connection.close()



# Call connect() Function
connect()
