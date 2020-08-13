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
    # Assigns the tuple given by fetchone() [or None] to
    # a variable so it can be accessed multiple times
    returnTuple = cursor.fetchone()
    # If there was no match, then return None before trying
    # to subscript a NoneType
    if (returnTuple == None):
        return None
    # This returns the first value of the tuple (the desired value)
    returnValue = returnTuple[0]
    return returnValue
