import sqlite3

# Creates table with specified name and column(s)
# Columns and their types are passed as keyword
# args as such: rank = "INTEGER", name = "TEXT"
def createTable(cursor, tableName, **kwargs):
    print("Creating " + tableName + " table...")
    createTableString = "CREATE TABLE "
    createTableString += tableName
    createTableString += " ("
    
    # Creats string listing column titles and types
    i = 0
    while i < (len(kwargs) - 1):
        createTableString += list(kwargs)[i] + " "
        createTableString += list(kwargs.values())[i] + ", "
        i += 1
    createTableString += list(kwargs)[i] + " "
    createTableString += list(kwargs.values())[i]
    createTableString += ")"

    # Execute the table creation
    cursor.execute(createTableString)


# Adds row to specified table with specified values
def insertRow(cursor, tableName, **kwargs):
    print("Adding row to " + tableName + " table...")
    insertRowString = "INSERT INTO "
    insertRowString += tableName
    insertRowString += " ("
    valuesArgs = "("
    
    # Creates strings from the keyword arguments that
    # SQLite can use as named parameters
    i = 0
    while i < (len(kwargs) - 1):
        insertRowString += list(kwargs)[i] + ", "
        valuesArgs += ":" + list(kwargs)[i] + ", "
        i += 1
    insertRowString += list(kwargs)[i] + ")"
    valuesArgs += ":" + list(kwargs)[i] + ")"
    insertRowString += " VALUES " + valuesArgs
    
    # kwargs is already a dictionary thanks to Python
    cursor.execute(insertRowString, kwargs)
    print("Added!")
