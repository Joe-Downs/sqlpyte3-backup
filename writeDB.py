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
