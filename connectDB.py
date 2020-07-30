import sqlite3

# Connects to given database; returns connection
def connectToDB(database):
    print("Connecting to the database " + database + "...")
    conn = sqlite3.connect(database)
    print("Database connected!")
    return conn

# Creates cursor for given connection; returns cursor
def createCursor(conn):
    print("Creating cursor...")
    cursor = conn.cursor()
    print("Cursor created!")
    return cursor

# Commits changes to the database for a given connection
def commitChanges(conn):
    print("Committing changes...")
    conn.commit()
    print("Changes committed!")

# Closes a given connection
def closeConnection(conn):
    print("Closing connection...")
    conn.close()
    print("Connection closed!")
