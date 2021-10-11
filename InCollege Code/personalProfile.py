import sqlite3
from getpass import getpass

conn = sqlite3.connect('PersonalProfile.db')
c = conn.cursor()

#Creates the Job DataBase with Tables if it does not exist
def create_profile_table():
    #SQL
    query = """CREATE TABLE IF NOT EXISTS PersonalProfile(userName TEXT,title TEXT, major TEXT, universityName TEXT, about TEXT)"""
    c.execute(query)
    conn.commit()
    query = """CREATE TABLE IF NOT EXISTS expierience(userName TEXT, jobId INT, title TEXT, employer TEXT, dateStart TEXT, dateEnd TEXT, location TEXT, description TEXT)"""
    c.execute(query)
    conn.commit()
    query = """CREATE TABLE IF NOT EXISTS education(userName TEXT, schoolName TEXT, degree TEXT, yearsAttended INT)"""
    c.execute(query)
    conn.commit() 


#Returns True if User is in Personal Profile Database
def hasProfile(userName):
    query = """SELECT * FROM PersonalProfile WHERE userName = ?"""
    data = (userName)
    c.execute(query, [data])
    x = c.fetchall()
    if x != []:
        return True

    return False

def getProfile(userName):
    query = """SELECT * FROM PersonalProfile WHERE userName = ?"""
    data = (userName)
    c.execute(query,[data])
    profile = c.fetchall()
    return profile

def hasJob(userName,jobId):
    query = """SELECT * FROM expierience WHERE userName = ? AND jobId = ?"""
    data = (userName,jobId)
    c.execute(query,data)
    x = c.fetchall()
    if x != []:
        return True

    return False

def getJob(userName, jobId):
    query = """SELECT * FROM expierience WHERE userName = ? AND jobId = ?"""
    data = (userName,jobId)
    c.execute(query,data)
    job = c.fetchall()
    return job

def hasSchool(userName):
    query = """SELECT * FROM education WHERE userName = ?"""
    data = (userName)
    c.execute(query,[data])
    x = c.fetchall()
    if x != []:
        return True

    return False

def getSchool(userName):
    query = """SELECT * FROM education WHERE userName = ?"""
    data = (userName)
    c.execute(query,[data])
    school = c.fetchall()
    return school

#Allows a field in the personal profile table to be updated given username and section
def update_profile(userName,section, newValue):
    if(section == "title"):
        query = """UPDATE PersonalProfile SET title = ? WHERE userName = ?"""
    elif(section == "major"):
        query = """UPDATE PersonalProfile SET major = ? WHERE userName = ?"""
    elif(section == "universityName"):
        query = """UPDATE PersonalProfile SET universityName = ? WHERE userName = ?"""
    elif(section == "about"):
        query = """UPDATE PersonalProfile SET about = ? WHERE userName = ?"""
    else:
        return -1
    
    data = (newValue,userName)
    c.execute(query,data)
    conn.commit()
    return 0


#Allows a field in the job table to be changed given a username and jobId and section
def update_job(userName,jobId,section,newValue):
    if(section == "title"):
            query = """UPDATE expierience SET title = ? WHERE userName = ? AND jobId = ?"""
    elif(section == "employer"):
        query = """UPDATE expierience SET employer = ? WHERE userName = ? AND jobId = ?"""
    elif(section == "dateStart"):
        query = """UPDATE expierience SET dateStart = ? WHERE userName = ? AND jobId = ?"""
    elif(section == "dateEnd"):
        query = """UPDATE expierience SET dateEnd = ? WHERE userName = ? AND jobId = ?"""
    elif(section == "location"):
        query = """UPDATE expierience SET location = ? WHERE userName = ? AND jobId = ?"""
    elif(section == "description"):
        query = """UPDATE expierience SET description = ? WHERE userName = ? AND jobId = ?"""
    else:
        return -1

    data = (newValue,userName,jobId)
    c.execute(query,data)
    conn.commit()
    return 0


#allows school table to be updated given username and section 
def update_school(userName,section,newValue):
    if(section == "schoolName"):
            query = """UPDATE education SET schoolName = ? WHERE userName = ?"""
    elif(section == "degree"):
        query = """UPDATE education SET degree = ? WHERE userName = ?"""
    elif(section == "yearsAttended"):
        query = """UPDATE education SET yearsAttended = ? WHERE userName = ?"""
    else:
        return -1

    data = (newValue,userName)
    c.execute(query,data)
    conn.commit()
    return 0

#Formats strings to have the first letter in uppercase of each word and the rest lowercase
def formatCaps(str):
    str = str.split(' ')
    result = ''
    for i in str:
        i = i.lower()
        tempUpper = i.upper()
        i = tempUpper[0] + i[1:] +" "
        result += i
    result = result[:-1]
    return result

#inserts username into job table, jobId should be labeled 1-3
def create_job(userName,jobId):
    query = """INSERT INTO expierience(userName , jobId , title , employer , dateStart , dateEnd , location , description ) VALUES(? , ? , ? , ? , ? , ? , ? , ? )"""
    data = (userName,jobId,None,None,None,None,None,None) 
    c.execute(query, data)
    conn.commit() 


#Adds user to school table    
def create_school(userName):
    query = """INSERT INTO education(userName, schoolName, Degree , yearsAttended) VALUES(?,?,?,?)"""
    data = (userName,None,None,None) 
    c.execute(query,data)
    conn.commit()
    
#Adds user to Personal Profile Table
def create_profile(userName):
    query = """INSERT INTO PersonalProfile(userName,title,major,universityName,about) VALUES(?,?,?,?,?)"""
    data = (userName,None,None,None,None) 
    c.execute(query,data)
    conn.commit()

def checkTitle(userName):
    for row in c.execute("""SELECT * FROM personalProfile"""):
        if userName == row[0] and row[1] != None:
            return True
    return False
def checkMajor(userName):
    for row in c.execute("""SELECT * FROM personalProfile"""):
        if userName == row[0] and row[2] != None:
            return True
    return False
def checkUniversityName(userName):
    for row in c.execute("""SELECT * FROM personalProfile"""):
        if userName == row[0] and row[3] != None:
            return True
    return False
def checkAbout(userName):
    for row in c.execute("""SELECT * FROM personalProfile"""):
        if userName == row[0] and row[4] != None:
            return True
    return False
def checkJob(userName):
    numjob = 0
    for row in c.execute("""SELECT * FROM experience"""):
        if userName == row[0] and row[1] != None:
            numjob +=1
    return numjob
def checkSchool(userName):
    for row in c.execute("""SELECT * FROM education"""):
        if userName == row[0]and row[1] != None:
            return True
    return False

def getProfileInfo(userName):
    # get all the information related to the given username
    query ="""SELECT * FROM personalProfile WHERE userName=?"""
    data = [userName]

    return c.execute(query, data)

def getExperienceInfo(userName):
    # get all the information related to the given username
    query = """SELECT * FROM expierience WHERE userName=?"""
    data = [userName]

    return c.execute(query, data)

def getEducationInfo(userName):
    # get all the information related to the given username
    query = """SELECT * FROM education WHERE userName=?"""
    data = [userName]

    return c.execute(query, data)