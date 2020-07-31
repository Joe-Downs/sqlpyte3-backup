import sqlite3

# Returns a single data value from a given table,
# column, and row
# e.g., return the rank for a given name
# or, return the name for a given rank
def getValue(cursor, tableName, desiredColumn,
             searchColumn, searchValue):
    selectDataString = "SELECT " + desiredColumn + " FROM " + tableName
    selectDataString += " WHERE " + searchColumn + "=?"
    cursor.execute(selectDataString, (searchValue,))
    # fetchone() returns tuple, this returns the first
    # value of that tuple (the desired value)
    returnValue = cursor.fetchone()[0]
    return returnValue
