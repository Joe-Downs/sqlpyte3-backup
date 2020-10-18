import sqlite3

# Returns a single data value from a given table,
# column, and row. Setting getMultiple to True will return a
# tuple of all the values which match the search parameters
# e.g., return the rank for a given name
# or, return the name for a given rank
def getValue(cursor, tableName, desiredColumn,
             searchColumn, searchValue, getMultiple = False):
    selectDataString = "SELECT " + desiredColumn + " FROM " + tableName
    selectDataString += " WHERE " + searchColumn + "=?"
    cursor.execute(selectDataString, (searchValue,))
    # Assigns the list of tuples given by fetchall() [or None] to
    # a variable so it can be accessed multiple times
    returnList = cursor.fetchall()
    # If there was no match, then return None before trying
    # to subscript a NoneType
    if (returnList == None):
        return None
    else:
        # We need to convert the list of tuples into a list of values
        for index in range(0, len(returnList)):
            returnList[index] = returnList[index][0]
    if getMultiple == True:
        # Return the whole list if the function call asks for multiple values
        return returnList
    else:
        # This returns the first value of the list (the desired value)
        return returnList[0]
