import sqlite3
from getpass import getpass

conn = sqlite3.connect('InCollege.db')
c = conn.cursor()

#Requests a friend
def requestFriend(userName,requestee):
    if findSpecificFriend(userName, requestee).fetchall() != []:
        return 0
    if findSpecificRequest(requestee,userName).fetchall() != []:
        return 1
    if findSpecificRequest(userName,requestee).fetchall() != []:
        #acceptRequest
        return 2
    query = """INSERT INTO requests(userName,requestee) VALUES(?,?)"""
    data = (userName,requestee)
    c.execute(query,data)
    conn.commit()
    return 3

#finds all friends of user, returns array containing username + name of friend for display
def findFriends(userName):
    query="""SELECT friend, firstname, lastname FROM friends f INNER JOIN Accounts a ON a.username = f.friend WHERE f.username = ?"""
    data = [userName]

    return c.execute(query,data).fetchall()

#checks if a specific friend is in the table
def findSpecificFriend(userName,friend):
    query = """SELECT friend FROM friends WHERE username = ? AND friend = ?"""
    data = [userName, friend]

    return c.execute(query, data)

#finds all friend requests for specific user
def findRequests(userName):
    query = """SELECT * FROM requests WHERE userName = ?"""
    data = (userName)
    return c.execute(query, [data])

#Frinds a specific friend request 
def findSpecificRequest(userName,requester):
    query = """SELECT * FROM requests WHERE userName = ? AND requestee = ?"""
    data = (userName,requester)
    return c.execute(query, data)

#PRIVATE METHOD: Deletes a request From requests table
def deleteRequest(userName,requester):
    query = """DELETE FROM requests WHERE userName  = ? AND requestee = ?"""
    data = (userName,requester)
    c.execute(query,data)
    conn.commit()
    return 1

#PRIVATE METHOD, Adds friend to friends table 
def addFriend(userName,friend):
    # insert current user and friend username pair
    query = """INSERT INTO friends(userName, friend) VALUES(?,?)"""
    data = (userName,friend)
    c.execute(query,data)
    conn.commit()

    # insert friend and current username pair
    query = """INSERT INTO friends(userName, friend) VALUES(?,?)"""
    data = (friend, userName)
    c.execute(query, data)
    conn.commit()
    return 1

#Accepts friend request (removes request and adds friends to friends table)
def acceptRequest(userName,requester):
    if findSpecificRequest(userName,requester).fetchall() == []:
        return 0
    deleteRequest(userName,requester)
    addFriend(userName, requester)
    return 1

#rejects a friend request
def rejectRequest(userName,requester):
    if findSpecificRequest(userName,requester).fetchall() == []:
        return 0
    deleteRequest(userName,requester)
    return 1

#removes a friend
def removeFriend(userName,friend):
    query = """DELETE FROM friends WHERE userName  = ? AND friend = ?"""
    data = (friend,userName)
    c.execute(query,data)
    conn.commit()

    query = """DELETE FROM friends WHERE userName  = ? AND friend = ?"""
    data = (userName,friend)
    c.execute(query,data)
    conn.commit()

    return 1

# get all the friend request for the specified username
def getAllFriendRequests(username):
    query = """SELECT r.username, r.requestee, a.firstname, a.lastname FROM requests r INNER JOIN Accounts a ON a.username = r.requestee  
                WHERE r.userName = ?"""
    data = [username]
    return c.execute(query, data)

# gets all the friends of the specified username with profiles
def getFriendsWithProfile(username):
    query = """SELECT friend, firstname, lastname FROM friends f INNER JOIN Accounts a ON a.username = f.friend WHERE f.username = ? AND friend IN (SELECT username FROM PersonalProfile)"""
    data = [username]
    return c.execute(query, data)

# gets the number of friends the specified username has
def getNumFriends(username):
    query = """SELECT COUNT(friend) FROM friends f INNER JOIN Accounts a ON a.username = f.friend WHERE f.username = ?"""
    data = [username]
    return c.execute(query, data)