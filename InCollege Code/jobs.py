import sqlite3
from getpass import getpass
from sqlite3.dbapi2 import Error

conn = sqlite3.connect('InCollege.db')
c = conn.cursor()


# /////////////////////////////////////////////////////////////////////////     ENTER DATA INTO DB     ////////////////////////////////////////////////////////////////////

# inserts login info from user into table
def job_data_entry(title, description, employer, location, salary, posterfirst, posterlast):
    # SQL
    query = """INSERT INTO Jobs(title, description, employer, location, salary, posterfirst, posterlast) VALUES(?, ?, ?, ?, ?, ?, ?);"""

    # Stores username, password , firstname , lastname
    data = (title, description, employer, location, salary, posterfirst, posterlast)
    c.execute(query, data)
    conn.commit()

# /////////////////////////////////////////////////////////////////////////     NUMBER OF JOBS    /////////////////////////////////////////////////////////////////////////

# number of jobs created
def job_created():
    # SQL
    rows = -1
    try:
        query = """SELECT * FROM Jobs"""
        c.execute(query)
        conn.commit()

        rows = len(c.fetchall())
    except Error:
        rows = 0
    return rows


# /////////////////////////////////////////////////////////////////////////     POST A JOB    ////////////////////////////////////////////////////////////////////////////

def postJob(posterfirst, posterlast):
    print("\nPost A Job.\n")

    ExistingJobs = 0

    if job_created() < 10:
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


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# username shows job selected, or returns "0" to go back
def list_jobs(username):
    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    jobs = c.execute("SELECT * FROM jobs").fetchall()
    store_list = []
    count = 1
    print("\n0. Back\n")
    for i in jobs:
        # sends title posted
        store_list.append(i)
        tmp = check_job_status(username, i[0])
        print(str(count) + ". " + "Title: " + str(i[1]) + "\n\tEmployer: " + str(i[3]) + "\n\tLocation: " + str(
            i[4]) + "\n\tSalary: " + str(i[5]) + "\n\tDescription: " + str(i[2]) + "\n\tStatus: " + str(tmp) + "\n")
        count += 1

    conn.close()

    return None

# //////////

def check_job_status(username, jobID):
    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    pnt = c.execute(
        "SELECT * FROM app_status WHERE (username = '{}' AND jobID = '{}' COLLATE NOCASE)".format(username, jobID)
    )
    check = str(pnt.fetchone())
    if check == "None":
        c.close()
        return None
    else:
        tmp = conn.execute(
            "SELECT * FROM app_status WHERE (username = '{}' AND jobID = '{}' COLLATE NOCASE)".format(
                username, jobID)
        ).fetchall()
        conn.close()
        # returns the status
        return str(tmp[0][2])

# /////////////

def apply_job(job, current_user, firstname, lastname):
    print("Apply for Jobs:")
    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    # checks poster
    poster = getPoster(job[0])
    if poster[1] == firstname and poster[2] == lastname:
        print("You cannot apply for a job you posted!\n")
        return False

    # checking if applied
    status = str(check_job_status(current_user, job[0]))
    if status == "applied":
        print("You already applied for this job!\n")
        return False
    elif status == "saved": # update the status of the job to applied
        c.execute(
            "UPDATE app_status SET status = 'applied' WHERE username = '{}' AND jobID = '{}'".format(current_user, job[0])
        )
    else:  # applied for a job
        c.execute("INSERT INTO app_status VALUES ('{}', '{}', 'applied')".format(current_user, job[0]))
        conn.commit()

    # inputs
    grad_date = input("Enter your graduation date (mm/dd/yyyy): ")
    start_date = input("Start date you can begin work (mm/dd/yyyy): ")
    story = input("Why should you get this position: ")

    # insert a row into applications table
    #c.execute("INSERT INTO applications VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(current_user, job[1], job[3], grad_date, start_date, story))
    c.execute("INSERT INTO applications VALUES ('{}', '{}', '{}', '{}', '{}')".format(current_user, job[0], grad_date, start_date, story))
    conn.commit()
    conn.close()
    return True

# checking if a job is deleted
def job_deleted(username):
    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    tmp = c.execute("SELECT * FROM app_status WHERE username = '{}' AND status = 'deleted'".format(username))
    if str(tmp.fetchone()) == "None":
        conn.close()
        return False
    else:
        c.execute("DELETE FROM app_status WHERE username = '{}' AND status = 'deleted'".format(username))
        conn.commit()
        conn.close()
    return True


# get all the job titles in the database
def getAllJobTitles():
    return c.execute("SELECT id, title FROM Jobs").fetchall()


# get the details of the specified job ID
def getJobDetails(id):
    return c.execute("SELECT * FROM Jobs WHERE id = ?", [id]).fetchone()


# get all the jobs posted by the given first name and last name
def getJobsByPoster(pFname, pLname):
    return c.execute("SELECT * FROM Jobs WHERE posterfirst = ? AND posterlast = ?", [pFname, pLname]).fetchall()


# delete a job in the database, including all the applications and remove the job from a user's saved list
def deleteJob(jobID):
    c.execute("DELETE FROM Jobs WHERE id = ?", [jobID])
    c.execute("UPDATE app_status SET status = 'deleted' WHERE jobID = ?",[jobID])
    c.execute("DELETE FROM SavedJobs WHERE jobID = ?", [jobID])  # delete rows from SavedJobs table
    conn.commit()
    return True


# look for a job by its title and delete that job
def deleteJobByTitle(title):
    c.execute("DELETE FROM Jobs WHERE title = ?", [title])
    conn.commit()
    return True


# add a job in the SavedJobs table
def saveJob(username, jobID):
    try:
        c.execute("INSERT INTO SavedJobs VALUES (?,?)", [username, jobID])
        c.execute("INSERT INTO app_status VALUES ('{}', '{}', 'saved')".format(username, jobID))
        conn.commit()
        return True
    except:
        return False


# remove a row from the SavedJobs table
def removeFromSavedJobs(username, jobID):
    c.execute("DELETE FROM app_status WHERE username = ? AND jobID = ?", [username, jobID])
    c.execute("DELETE FROM SavedJobs WHERE username = ? AND jobID = ?", [username, jobID])
    conn.commit()
    return True


# get all the rows in SavedJobs associated with the given username
def getAllSavedJobs(username):
    return c.execute("SELECT j.id, j.title, j.description, j.employer, j.location, j.salary, j.posterfirst, j.posterlast FROM SavedJobs s INNER JOIN Jobs j ON s.jobID = j.id "
                     "WHERE username = ?", [username]).fetchall()


# get the poster of the given job ID
def getPoster(jobID):
    return c.execute("SELECT id, posterfirst, posterlast FROM Jobs WHERE id = ?", [jobID]).fetchone()


# get the rows associated with the username given from the app_status table
def getDeletedApplications(username):
    return c.execute("SELECT * FROM app_status WHERE username = ? AND status = 'deleted'", [username]).fetchall()

# gets all the job titles the given username has applied for
def getAllJobTitlesAppliedFor(username):
    return c.execute("SELECT j.id, j.title FROM Jobs j INNER JOIN app_status a ON j.id = a.jobID WHERE status == 'applied' AND a.username = ?", [username]).fetchall()