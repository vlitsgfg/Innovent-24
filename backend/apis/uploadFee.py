import xlrd
import mysql.connector
import os

# Open the workbook and define the worksheet
def insertInToSql(f):
    f.save(f.filename)
    book = xlrd.open_workbook(f.filename)
    sheet = book.sheet_by_name('Sheet1')

    # Establish a MySQL connection
    database = mysql.connector.connect (host="localhost", user = "root", db = "fee")

    # Get the cursor, which is used to traverse the database, line by line
    cursor = database.cursor()

    # Create the INSERT INTO SQL query
    query = "INSERT INTO DAILY_FEES (ID,REGNO,NAME,YEAR,BRANCH,PYEAR,AMOUNT,DATE,TIME,DESCRIPTION) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    # Create a For loop to iterate through each row in the XLS file
    for r in range(1,sheet.nrows):
        ID = sheet.cell(r,0).value

        REDGNO = sheet.cell(r,1).value

        NAME = sheet.cell(r,2).value
        
        YEAR = sheet.cell(r,3).value
        
        BRANCH = sheet.cell(r,4).value
        
        PYEAR = sheet.cell(r,5).value

        AMOUNT = sheet.cell(r,6).value

        DATE = sheet.cell(r,7).value
        
        TIME = sheet.cell(r,8).value
        
        DESCRIPTION = sheet.cell(r,9).value
    # Assign values from each row        
        values = (ID,REDGNO,NAME,YEAR,BRANCH,PYEAR,AMOUNT,DATE,TIME,DESCRIPTION)
        print(values)
        #Execute sql Query
        cursor.execute(query, values)

    # Close the cursor
    cursor.close()

    # Commit the transaction
    database.commit()

    # Close the database connection
    database.close()
    os.remove(f.filename)
    return True