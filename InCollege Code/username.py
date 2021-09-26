

#getting A DB for creating User name tables and access the table 


import sqlite3
from getpass import getpass

conn = sqlite3.connect('Username.db')
c = conn.cursor()

#table creation for Username table ?
def create_table():
    #SQL
    query = """CREATE TABLE IF NOT EXISTS Username(username TEXT, password TEXT,firstname TEXT,lastname TEXT)"""
    c.execute(query)
    conn.commit()



    #inserts login info from user into table
def data_entry(username, password,firstname,lastname):
    #SQL
    query = """INSERT INTO Username (username, password,firstname,lastname) VALUES(?, ?,?,?);"""
    
    #Stores username, password , firstname , lastname 
    data = (username, password,firstname,lastname)
    c.execute(query, data)
    conn.commit()

    #validating whether username unique 

def look_value(username):
    username2 = username

    target = (username,)
    #SQL
    query = """SELECT * FROM Username WHERE username = ?;"""
    c.execute(query, target)
    conn.commit()
    tuples = c.fetchall()
    while len(tuples) > 0:

        print("exists")

        username2 = input("Username: ")
        target = (username2,)


        c.execute(query, target)
        conn.commit()
        tuples = c.fetchall()


    if len(tuples) == 0 and username == username2:
        return username
    elif len(tuples) == 0 and username != username2:
        return username2


#number of accounts created 
def number_rows():
    #SQL
    query = """SELECT * FROM Username"""
    c.execute(query)
    conn.commit()
    
    rows = len(c.fetchall())
    return rows
    

#search for exciting User 
def find_user(first_name,last_name):
    
    for row in c.execute("""SELECT * FROM Username"""):
        if first_name == row[2] and last_name == row[3]:
            print("User found")
            return
    print("User not found ")

#Login attempt for exciting account 
def login(username, password):
    #SQL
    query = """SELECT * FROM Username WHERE username = ? AND password = ?;"""
    data = (username, password)

    c.execute(query, data)
    conn.commit()
    tuple = c.fetchall()
   
    return len(tuple) != 0
