import sqlite3
from getpass import getpass

conn = sqlite3.connect('Jobs.db')
c = conn.cursor()

#/////////////////////////////////////////////////////////////////////////     CREATE DB     //////////////////////////////////////////////////////////////////////////////

#table creation for Username table ?
def create_job_table():
    #SQL
    query = """CREATE TABLE IF NOT EXISTS Jobs(title TEXT, description TEXT, employer TEXT, location TEXT, salary TEXT, posterfirst TEXT, posterlast TEXT)"""
    c.execute(query)
    conn.commit()

#/////////////////////////////////////////////////////////////////////////     ENTER DATA INTO DB     ////////////////////////////////////////////////////////////////////

#inserts login info from user into table
def job_data_entry(title, description, employer, location, salary, posterfirst, posterlast):
    #SQL
    query = """INSERT INTO Jobs (title, description, employer, location, salary, posterfirst, posterlast) VALUES(?, ?, ?, ?, ?, ?, ?);"""
    
    #Stores username, password , firstname , lastname 
    data = (title, description, employer, location, salary, posterfirst, posterlast)
    c.execute(query, data)
    conn.commit()

#/////////////////////////////////////////////////////////////////////////     NUMBER OF JOBS    /////////////////////////////////////////////////////////////////////////

#number of jobs created 
def job_created():
    #SQL
    query = """SELECT * FROM Jobs"""
    c.execute(query)
    conn.commit()
    
    rows = len(c.fetchall())
    return rows

#/////////////////////////////////////////////////////////////////////////     POST A JOB    ////////////////////////////////////////////////////////////////////////////

def postJob(posterfirst, posterlast):
    
    print("\nPost A Job.\n")

    if job_created() < 5:
        title = input("Enter Job Title: ")
        description = input("Enter Job Description: ")
        employer = input("Enter Employer Name: ")
        location = input("Enter Location: ")
        salary = input("Enter Salary: ")

        job_data_entry(title, description, employer, location, salary, posterfirst, posterlast)

        print("Successfully added a job.\n")
    else:
        print("Job limit has been reached please try again later.\n")
    return 0

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////