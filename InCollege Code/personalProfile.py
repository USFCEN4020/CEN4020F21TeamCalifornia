import sqlite3
from getpass import getpass

conn = sqlite3.connect('PersonalProfile.db')
c = conn.cursor()

def create_job_table():
    #SQL
    query = """CREATE TABLE IF NOT EXISTS PersonalProfile(userName TEXT,title TEXT, major TEXT, universityName TEXT, about TEXT)"""
    c.execute(query)
    conn.commit()
    query = """CREATE TABLE IF NOT EXISTS expierience(userName TEXT, jobNum INT, title TEXT, employer TEXT, dateStart Text, dateEnd Text, location TEXT, description TEXT)"""
    c.execute(query)
    conn.commit()
    query = """CREATE TABLE IF NOT EXISTS education(userName TEXT, schoolName Text, Degree TEXT, yearsAttended INT)"""
    c.execute(query)
    conn.commit() 
def hasProfile(userName):
    for row in c.execute("""SELECT * FROM PersonalProfile"""):
        if(userName == row[0]):
            return True
    return False

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

def update_job(userName,jobId,section,newValue):
    if(section == "title"):
            query = """UPDATE PersonalProfile SET title = ? WHERE userName = ?"""
    elif(section == "employer"):
        query = """UPDATE PersonalProfile SET employer = ? WHERE userName = ?"""
    elif(section == "dateStart"):
        query = """UPDATE PersonalProfile SET dateStart = ? WHERE userName = ?"""
    elif(section == "dateEnd"):
        query = """UPDATE PersonalProfile SET dateEnd = ? WHERE userName = ?"""
    elif(section == "location"):
        query = """UPDATE PersonalProfile SET location = ? WHERE userName = ?"""
    elif(section == "description"):
        query = """UPDATE PersonalProfile SET description = ? WHERE userName = ?"""
    else:
        return -1

    data = (newValue,userName)
    c.execute(query,data)
    conn.commit()
    return 0

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

def create_job(userName,jobId):
    query = """INSERT INTO expierience(userName TEXT, jobNum INT, title TEXT, employer TEXT, dateStart Text, dateEnd Text, location TEXT, description TEXT) VALUES(?,?,?,?,?,?,?,?)"""
    data = (userName,jobId,None,None,None,None,None,None) 
    c.execute(query,data)
    conn.commit() 

    title = input("enter Title for profile or 0 to quit")
    if title == '0':
        return 0
    update_job(userName,jobId,'title',title)

    employer = input("Enter your employer or 0 to quit")
    if employer == '0':
        return 1
    
    update_job(userName,jobId,"employer",employer)

    dateStart = input("Enter the Date you started the job or 0 to quit")
    if dateStart == '0':
        return 2

    update_job(userName,jobId,'dateStart',dateStart)


    dateEnd = input("Enter the Date you ended the job or 0 to quit")
    if dateEnd == '0':
        return 3

    update_job(userName,jobId,'dateEnd',dateEnd)

    location = input("Enter the location of the job or 0 to quit")
    if location == '0':
        return 4
    update_job(userName,jobId,'location',location)
    
    description = input("Enter a description for the job or 0 to quit")
    if description == '0':
        return 2
    
    update_job(userName,jobId,'description',description)
    

def create_profile(userName):
    query = """INSERT INTO PersonalProfile(userName,title,major,universityName,about) VALUES(?,?,?,?,?)"""
    data = (userName,None,None,None,None) 
    c.execute(query,data)
    conn.commit()

    title = input("enter Title for profile or 0 to quit")
    if title == '0':
        return 0
    update_profile(userName,'title',title)

    major = input("Enter your Major or 0 to quit")
    if major == '0':
        return 1
    
    major = formatCaps(major)

    update_profile(userName,"major",major)

    uniName = input("Enter Name of your University or 0 to quit")
    if uniName == '0':
        update_profile(title,major,None,None)
        return 2

    uniName = formatCaps(uniName)

    update_profile(userName,"universityName",uniName)

    about = input("Enter info about you or 0 to quit")
    if about == '0':
        
        return 3 

    update_profile(userName,"about",about)

    jobOption = input("You can create up to three jobs, would you like to create one?\n(y,n)")
    if jobOption == 'y':
        create_job(userName,1)
        jobOption = input("Would you like to create a second Job?\n(y,n)")
        if jobOption == 'y':
            create_job(userName,2)
            jobOption = input("Would you like to create a third Job?\n(y,n)")
            if jobOption == 'y':
                create_job(userName,3)
    



    
    

