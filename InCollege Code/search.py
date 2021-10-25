from verify_acc import *
from personalProfile import hasProfile

#/////////////////////////////////////////////////////////////////////////     FIND USERS     /////////////////////////////////////////////////////////////////////////

# search for existing users that satisfy ANY of the criteria: first_name, last_name, university, and major
def find_users(toFind, currUser):
    users = []

    if currUser == '': # user is not logged in
        data = ['%'+toFind+'%', '%'+toFind+'%', '%'+toFind+'%', '%'+toFind+'%']
        query = """SELECT a.username, firstname, lastname, major, universityName FROM Accounts a LEFT JOIN PersonalProfile p ON a.username = p.userName
                WHERE a.username LIKE ? OR lastname LIKE ? OR major LIKE ? OR universityName LIKE ?"""
    else: # do not display the currently logged in user in the results
        data = [currUser, '%'+toFind+'%', '%'+toFind+'%', '%'+toFind+'%', '%'+toFind+'%']
        query = """SELECT a.username, firstname, lastname, major, universityName FROM Accounts a LEFT JOIN PersonalProfile p ON a.username = p.userName
                    WHERE a.username != ? AND (a.username LIKE ? OR lastname LIKE ? OR major LIKE ? OR universityName LIKE ?)"""

    for row in c.execute(query, data):
        if row not in users:
            users.append(row)

    return users

#/////////////////////////////////////////////////////////////////////////     FIND USER     /////////////////////////////////////////////////////////////////////////

#search for a user based on their first name and last name
def find_user(first_name, last_name):
    data = [first_name, last_name]
    for row in c.execute("""SELECT * FROM Accounts WHERE first_name = ? AND last_name = ?""", data):
        print("\nThey are a part of the InCollege system.\n")
        return True
    print("\nThey are not yet a part of the InCollege system.\n")
    return False

#/////////////////////////////////////////////////////////////////////////     SEARCH PEOPLE     /////////////////////////////////////////////////////////////////////

def searchPeople(currUser):

    print("\nSearch For A Person.\n")

    toFind = input("Please enter the last name, university or major of the person you're searching for: ")

    users = find_users(toFind,currUser)
    print("\nSearch Results: \n")

    if len(users) > 0:
        for u in users:
            displayUserInfo(u[0])
        return True
    else:
        print("No users found.\n")
        return False

#/////////////////////////////////////////////////////////////////////////     DISPLAY USER     /////////////////////////////////////////////////////////////////////

# display all the relevant user information
def displayUserInfo(username):
    data = [username]
    for u in c.execute("""SELECT a.username, firstname, lastname, major, universityName FROM Accounts a LEFT JOIN PersonalProfile p ON a.username = p.userName WHERE a.username = ?""", data):
        if (hasProfile(u[0])):
            print(u[1] + " " + u[2] + "\nUsername: " + u[0] + "\nMajor: " + u[3] + "\nSchool: " + u[4] + "\n")
        else:
            print(u[1] + " " + u[2] + "\nUsername: " + u[0] + "\n")

#/////////////////////////////////////////////////////////////////////////     CURRENT USER     /////////////////////////////////////////////////////////////////////

def current_user(username, password):

    for row in c.execute("""SELECT * FROM Accounts"""):
        if username == row[0] and password == row[1]:
            user = [row[0], row[1], row[2], row[3]]
    return user

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
