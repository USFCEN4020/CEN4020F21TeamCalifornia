#imports all functions from verify_acc.py
from verify_acc import *

#/////////////////////////////////////////////////////////////////////////     FIND USER     /////////////////////////////////////////////////////////////////////////
#search for exciting User 
def find_user(first_name,last_name):
    
    for row in c.execute("""SELECT * FROM Accounts"""):
        if first_name == row[2] and last_name == row[3]:
            print("\nThey are a part of the InCollege system.\n")
            return True
    print("\nThey are not yet a part of the InCollege system.\n")
    return False

#/////////////////////////////////////////////////////////////////////////     SEARCH PEOPLE     /////////////////////////////////////////////////////////////////////

def searchPeople():
    print("\nSearch For A Person.\n")

    print("Please enter the first and last name of the person you wish to search for.\n")

    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")

    if find_user(first_name,last_name):
        return True
    return False

#/////////////////////////////////////////////////////////////////////////     CURRENT USER     /////////////////////////////////////////////////////////////////////

def current_user(username, password):
    
    for row in c.execute("""SELECT * FROM Accounts"""):
        if username == row[0] and password == row[1]:
            user = [row[0], row[1], row[2], row[3]]
    return user
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
