import sqlite3
from getpass import getpass

conn = sqlite3.connect('Accounts.db')
c = conn.cursor()

#/////////////////////////////////////////////////////////////////////////     CREATE DB     //////////////////////////////////////////////////////////////////////////////

#table creation for Username table ?
def create_table():
    #SQL
    query = """CREATE TABLE IF NOT EXISTS Accounts(username TEXT, password TEXT,firstname TEXT,lastname TEXT, email INTEGER, sms INTEGER, ads INTEGER, language TEXT)"""
    c.execute(query)
    conn.commit()

#/////////////////////////////////////////////////////////////////////////     ENTER DATA INTO DB     ////////////////////////////////////////////////////////////////////

#inserts login info from user into table
def data_entry(username, password,firstname,lastname,email,sms,ads,language):
    #SQL
    query = """INSERT INTO Accounts (username, password,firstname,lastname,email,sms,ads,language) VALUES(?, ?,?,?,?,?,?,?);"""
    
    #Stores username, password , firstname , lastname 
    data = (username, password,firstname,lastname,email,sms,ads,language)
    c.execute(query, data)
    conn.commit()

#/////////////////////////////////////////////////////////////////////////     LOGIN ATTEMPT    //////////////////////////////////////////////////////////////////////////

#Login attempt for exciting account 
def login(username, password):
    #SQL
    query = """SELECT * FROM Accounts WHERE username = ? AND password = ?;"""
    data = (username, password)

    c.execute(query, data)
    conn.commit()
    tuple = c.fetchall()
   
    return len(tuple) != 0

#/////////////////////////////////////////////////////////////////////////     NUMBER OF ACCOUNTS     ///////////////////////////////////////////////////////////////////////

#number of accounts created 
def number_rows():
    #SQL
    query = """SELECT * FROM Accounts"""
    c.execute(query)
    conn.commit()
    
    rows = len(c.fetchall())
    return rows

#/////////////////////////////////////////////////////////////////////////     CHECK UNIQUE USERNAME     ////////////////////////////////////////////////////////////////////

#search for exciting User 
def unique_user(username):
    
    for row in c.execute("""SELECT * FROM Accounts"""):
        if username == row[0]:
            return True
    return False

#/////////////////////////////////////////////////////////////////////////     CHECK PASSWORD    ///////////////////////////////////////////////////////////////////////////

# Function to validate the password
def password_check(passwd):
    # declaring the special characters to be used to enter by user

    SpecialSym = ['$', '@', '#', '%']

    # variable used to determine the valid characters within the loop
    val = True

    # beginning of the loop

    # checks the minimum length validation
    if len(passwd) < 8:
        print('length should be at least 8')
        val = False

    # checks the max length validation
    if len(passwd) > 12:
        print('length should be not be greater than 12')
        val = False

    # checks for 1 digit input
    if not any(char.isdigit() for char in passwd):
        print('Password should have at least one digit')
        val = False

    # checks for Upper case input
    if not any(char.isupper() for char in passwd):
        print('Password should have at least one uppercase letter')
        val = False

    # checks for special synbol inout
    if not any(char in SpecialSym for char in passwd):
        print('Password should have at least one of the symbols $@#')
        val = False

    # # checks if inputs are valid
    # if val:
    #     return val
    return val

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def getAccountInfo(username):
    # get all the information associated with the given username
    query = """SELECT * FROM Accounts WHERE username = ?"""
    data = [username]
    return c.execute(query, data)