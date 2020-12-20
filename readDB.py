import sqlite3

# Returns a single data value from a given table,
# column, and row. Setting getMultiple to True will return a
# list of all the values which match the search parameters. Setting
# sortedResults to True will sort the returned data by the values
# in a given column (ascending, by default)
# e.g., return the rank for a given name
# or, return the name for a given rank
def getValue(cursor, tableName, desiredColumn,
             searchColumn, searchValue, getMultiple = False,
             sortedResults = False, sortBy = "", descending = False):
    selectDataString = "SELECT " + desiredColumn + " FROM " + tableName
    selectDataString += " WHERE " + searchColumn + "=?"
    if sortedResults == True:
        # Sort the results by the given colum in the call requests it
        # The order is ascending by default
        selectDataString += f"ORDER BY {sortBy} "
        if descending == True:
            # Sort the results in descending order
            selectDataString += f"DESC"
    cursor.execute(selectDataString, (searchValue,))
    # Assigns the list of tuples given by fetchall() [or None] to
    # a variable so it can be accessed multiple times
    returnList = cursor.fetchall()
    # If there was no match, then return None before trying,
    # raise an error explaining
    if (len(returnList) == 0):
        raise sqlite3.ProgrammingError(f"{desiredColumn} for {searchColumn} {searchValue} was not found")
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
