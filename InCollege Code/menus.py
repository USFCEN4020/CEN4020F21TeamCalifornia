# imports all functions from messages.py
from messages import *
# imports all functions from search.py
from search import *
# imports all functions from jobs.py
from jobs import *
# imports all functions from update_acc.py
from update_acc import *
# imports all functions from personalProfile.py
from personalProfile import *
# imports all functions from friends.py
from friends import *

# username, password, first name, last name
logged_in = []


# /////////////////////////////////////////////////////////////////////////     LOGIN MENU     /////////////////////////////////////////////////////////////////////////

def loginMenu():
    print("\nLog In to InCollege\n")

    if number_rows() == 0:
        print("No users in the system. Please create an account.")
        return

    found = False

    while not found:  # continue looping as long as user inputs invalid login info
        # get input from the user
        username = input("Enter username: ")
        password = input("Enter password: ")

        # check if username and password are valid
        found = login(username, password)
        if not found:
            print("Incorrect username/password, please try again\n")
    print("\nYou have successfully logged in\n")
    global logged_in
    # gets the first and last name of the current user that is logged in
    logged_in = current_user(username, password)
    mainMenu()


# /////////////////////////////////////////////////////////////////////////     HOME MENU     /////////////////////////////////////////////////////////////////////////

def homeMenu():
    print("Welcome to InCollege.")
    # prints the student success story found on messages.py
    printStudentSuccess()

    # Creates a database for the profiles if one doesnt exisit
    create_tables()

    while True:

        # prints the home menu
        printHomeMenu()

        # gets user input
        select = input("Enter command: ")

        if (
                select == "1" or select == "2" or select == "3" or select == "4" or select == "0" or select == "5" or select == "6"):
            break
        else:
            # if user inputs an incorrect value an this function prints an error message
            printInvalidEntry()
            continue

    if (select == "1"):
        loginMenu()  # redirect the user to log in menu
    elif (select == "2"):
        createAccountMenu()  # redirect the user to register menu
    elif (select == "3"):
        if searchPeople(''):
            print("Please login to add people as a friend. Thank you.\n")
    elif (select == "4"):
        print("\nVideo is now playing...\n")
    elif (select == "5"):
        usefulLinksMenu()
    elif (select == "6"):
        impLinksMenu()
    elif (select == "0"):
        print("Thank you for using InCollege!")
        quit()
    else:
        printInvalidEntry()


# /////////////////////////////////////////////////////////////////////     CREATE ACCOUNT MENU     ////////////////////////////////////////////////////////////////////

def createAccountMenu():
    print("\nCreate a New Account\n")

    if number_rows() < 10:
        username = input("Enter username: ")
        password = input("Enter password: ")
        firstname = input("Enter First Name: ")
        lastname = input("Enter Last Name: ")

        # check if username is unique and password is valid
        if not unique_user(username) and password_check(password):
            data_entry(username, password, firstname, lastname, 1, 1, 1, "English")
            print("Successfully created an account\n")
    else:
        print("All permitted accounts have been created, please come back later\n")
    return 0


# /////////////////////////////////////////////////////////////////////////     MAIN MENU     /////////////////////////////////////////////////////////////////////////

def mainMenu():
    while True:
        global logged_in

        # prints the main menu
        printMainMenu(logged_in[0])
        # gets user input

        if findRequests(logged_in[0]).fetchall() != []:
            printHasRequest()

        opt = input("Enter command: ")

        if int(opt) == 1:  # search for job
            jobMenu()
        elif int(opt) == 2:  # search for a user
            if searchPeople(logged_in[0]):
                addFriendMenu(logged_in[0])
        elif int(opt) == 3:  # learn a new skill
            skillMenu()
        elif int(opt) == 4:
            usefulLinksMenu()
        elif int(opt) == 5:
            impLinksMenu()
        elif int(opt) == 6:
            friendsMenu()
        elif int(opt) == 7:
            if hasProfile(logged_in[0]):
                # update/edit profile Function goes here
                editProfile()  # temp value for code to work
            else:
                # Creates profile if one does not exist.
                createProfileMenu()
        elif int(opt) == 8:
            if hasProfile(logged_in[0]):
                viewProfile(logged_in[0])
            else:
                print("You have not created a profile. Please create one first.\n")
        elif int(opt) == 0:

            logged_in = []
            print("You have sucessfully logged out!\n")
            break
        else:
            printInvalidEntry()
    return 0


# /////////////////////////////////////////////////////////////////////////     SKILL MENU     /////////////////////////////////////////////////////////////////////////

def skillMenu():
    while True:
        # prints the list of skills
        printSkillList()
        # gets user input
        skill = input("Select a skill: ")

        if skill != "0":
            # prints an under construction message
            printUnderConstruction()
        elif skill == "0":
            break
        else:
            printInvalidEntry()
    return 0


# /////////////////////////////////////////////////////////////////////////     JOB MENU     ///////////////////////////////////////////////////////////////////////////

def jobMenu():
    while True:
        print("\nJob search/internship.\n")

        printJobMenu()

        if checkDeletedApplications(logged_in[0]):
            print("One or more of the jobs you have applied for has been deleted.")

        select = input("Enter Command: ")

        if select == "1":  # post a job
            postJob(logged_in[2], logged_in[3])
        elif select == "2":   # view all job titles
            viewJobTitles()
        elif select == "3":  # view all the jobs the currently logged in user has posted
            viewAllPostedJobs(logged_in[2], logged_in[3])
        elif select == "4":   # delete a job
            viewAllPostedJobs(logged_in[2], logged_in[3])
            deleteJobMenu(logged_in[2], logged_in[3])
        elif select == "5":
            viewSavedJobs(logged_in[0])  # view currently logged in user's saved jobs
        elif select == "6":
            displayAllJobTitlesAppliedFor(logged_in[0])
        elif select == "0":
            break
        else:
            printInvalidEntry()

    return


# /////////////////////////////////////////////////////////////////////////     USEFUL LINKS MENU     /////////////////////////////////////////////////////////////////////////

def usefulLinksMenu():
    while True:
        printUsefulLinksMenu()

        # gets user input
        opt = input("Enter command: ")

        if int(opt) == 1:
            usefulGeneralGroup()
        elif int(opt) == 2:
            printUnderConstruction()
        elif int(opt) == 3:
            printUnderConstruction()
        elif int(opt) == 4:
            printUnderConstruction()
        elif int(opt) == 0:
            break
        else:
            printInvalidEntry()
    return 0


# /////////////////////////////////////////////////////////////////////////     IMPORTANT LINKS MENU     /////////////////////////////////////////////////////////////////////////

def impLinksMenu():
    while True:
        printImpLinksMenu()

        # gets user input
        opt = input("Enter command: ")

        if int(opt) == 1:
            usefulGeneralGroup()
        elif int(opt) == 2:
            print(
                "In College: Welcome to In College, the world's largest college student network with many users in many countries and territories worldwide\n")
        elif int(opt) == 3:
            print("The assessibiliy of our app is not limited\n")
        elif int(opt) == 4:
            print("User need to agree terms to join in this application\n")
        elif int(opt) == 5:
            privacyPolicyMenu()
        elif int(opt) == 6:
            print("User need to accept the cookie policy\n")
        elif int(opt) == 7:
            print("User will need to acknowledge the copyright policy\n")
        elif int(opt) == 8:
            print("User will need to acknowledge the brand policy\n")
        elif int(opt) == 9:
            guestControlMenu()
        elif int(opt) == 10:
            languageMenu()
        elif int(opt) == 0:
            break
        else:
            printInvalidEntry()

    return 0


# /////////////////////////////////////////////////////////////////////////     USEFUL GENERAL GROUP MENU     ////////////////////////////////////////////////////////////////////

def usefulGeneralGroup():
    while True:
        printUsefulGeneralGroup()

        # gets user input
        opt = input("Enter command: ")

        if int(opt) == 1:
            createAccountMenu()
        elif int(opt) == 2:
            print("We're here to help")
        elif int(opt) == 3:
            print(
                "In College: Welcome to In College, the world's largest college student network with many users in many countries and territories worldwide")
        elif int(opt) == 4:
            print("In College Pressroom: Stay on top of the latest news, updates, and reports")
        elif int(opt) == 5:
            printUnderConstruction()
        elif int(opt) == 6:
            printUnderConstruction()
        elif int(opt) == 7:
            printUnderConstruction()
        elif int(opt) == 0:
            break
        else:
            printInvalidEntry()

    return 0


# /////////////////////////////////////////////////////////////////////////     PRIVACY POLICY MENU     /////////////////////////////////////////////////////////////////////////
def privacyPolicyMenu():
    while True:
        printPrivacyPolicyMenu()

        # gets user input
        opt = input("Enter command: ")

        if int(opt) == 1:
            printUnderConstruction()
        elif int(opt) == 2:
            guestControlMenu()
        elif int(opt) == 0:
            break
        else:
            printInvalidEntry()
    return


# /////////////////////////////////////////////////////////////////////////     GUEST CONTROL MENU     //////////////////////////////////////////////////////////////////////////

def guestControlMenu():
    if logged_in == []:
        print("\n Please login to change settings.\n")
    else:
        while True:
            printGuestControlMenu()

            # gets user input
            opt = input("Enter command: ")

            if int(opt) == 1:
                update_email_option(logged_in[0], logged_in[1])
            elif int(opt) == 2:
                update_sms_option(logged_in[0], logged_in[1])
            elif int(opt) == 3:
                update_ad_option(logged_in[0], logged_in[1])
            elif int(opt) == 4:
                languageMenu()
            elif int(opt) == 0:
                break
            else:
                printInvalidEntry()
    return


# /////////////////////////////////////////////////////////////////////////     LANGUAGE MENU     //////////////////////////////////////////////////////////////////////////

def languageMenu():
    if logged_in == []:
        print("\n Please login to change settings.\n")
    else:
        while True:
            printLanguageMenu()

            # gets user input
            opt = input("Enter command: ")

            if int(opt) == 1:
                update_lang_option(logged_in[0], logged_in[1], "English")
            elif int(opt) == 2:
                update_lang_option(logged_in[0], logged_in[1], "Spanish")
            elif int(opt) == 0:
                break
            else:
                printInvalidEntry()
    return


# /////////////////////////////////////////////////////////////////////////////     Create Job Menu     //////////////////////////////////////////////////////////////////

def createJobMenu(jobId):
    create_job(logged_in[0], jobId)

    title = input("Enter Title for profile or 0 to quit: ")
    if title == '0':
        return 0
    update_job(logged_in[0], jobId, 'title', title)

    employer = input("Enter your employer or 0 to quit: ")
    if employer == '0':
        return 1

    update_job(logged_in[0], jobId, "employer", employer)

    dateStart = input("Enter the Date you started the job or 0 to quit: ")
    if dateStart == '0':
        return 2

    update_job(logged_in[0], jobId, 'dateStart', dateStart)

    dateEnd = input("Enter the Date you ended the job or 0 to quit: ")
    if dateEnd == '0':
        return 3

    update_job(logged_in[0], jobId, 'dateEnd', dateEnd)

    location = input("Enter the location of the job or 0 to quit: ")
    if location == '0':
        return 4
    update_job(logged_in[0], jobId, 'location', location)

    description = input("Enter a description for the job or 0 to quit: ")
    if description == '0':
        return 2

    update_job(logged_in[0], jobId, 'description', description)


# /////////////////////////////////////////////////////////////////////////////////////   Create School Menu   /////////////////////////////////////////////////////////////

def createSchoolMenu():
    create_school(logged_in[0])
    schoolName = input("Enter the Name for your school or 0 to quit: ")
    if schoolName == '0':
        return 0
    update_school(logged_in[0], "schoolName", schoolName)
    degree = input("Enter the degree you got from your school or 0 to quit: ")
    if degree == '0':
        return 1
    update_school(logged_in[0], "degree", degree)
    yearsAttended = input("Enter the number of years you attened the school or 0 to quit: ")
    if yearsAttended == '0':
        return 2
    update_school(logged_in[0], "yearsAttended", int(yearsAttended))

    return 3

# ///////////////////////////////////////////////////////////////////////////////////////    Create Profile Menu    ///////////////////////////////////////////////////////

def createProfileMenu():
    create_profile(logged_in[0])

    title = input("enter Title for profile or 0 to quit: ")
    if title == '0':
        return 0
    update_profile(logged_in[0], 'title', title)

    major = input("Enter your Major or 0 to quit: ")
    if major == '0':
        return 1

    major = formatCaps(major)

    update_profile(logged_in[0], "major", major)

    uniName = input("Enter Name of your University or 0 to quit: ")
    if uniName == '0':
        update_profile(title, major, None, None)
        return 2

    uniName = formatCaps(uniName)

    update_profile(logged_in[0], "universityName", uniName)

    about = input("Enter info about you or 0 to quit: ")
    if about == '0':
        return 3

    update_profile(logged_in[0], "about", about)

    jobOption = input("You can create up to three jobs, would you like to create one?\n(y or n): ")
    if jobOption == 'y':
        createJobMenu(1)
        jobOption = input("Would you like to create a second job?\n(y,n): ")
        if jobOption == 'y':
            createJobMenu(2)
            jobOption = input("Would you like to create a third job?\n(y,n): ")
            if jobOption == 'y':
                createJobMenu(3)

    schoolOption = input("Would you like to enter a school? \n(y or n): ")
    if (schoolOption == 'y'):
        createSchoolMenu()
    return 4


def updateJobMenu(jobId):
    title = input("enter Title for profile or 0 to quit: ")
    if title == '0':
        return 0
    update_job(logged_in[0], jobId, 'title', title)

    employer = input("Enter your employer or 0 to quit: ")
    if employer == '0':
        return 1

    update_job(logged_in[0], jobId, "employer", employer)

    dateStart = input("Enter the Date you started the job or 0 to quit: ")
    if dateStart == '0':
        return 2

    update_job(logged_in[0], jobId, 'dateStart', dateStart)

    dateEnd = input("Enter the Date you ended the job or 0 to quit: ")
    if dateEnd == '0':
        return 3

    update_job(logged_in[0], jobId, 'dateEnd', dateEnd)

    location = input("Enter the location of the job or 0 to quit: ")
    if location == '0':
        return 4
    update_job(logged_in[0], jobId, 'location', location)

    description = input("Enter a description for the job or 0 to quit: ")
    if description == '0':
        return 2

    update_job(logged_in[0], jobId, 'description', description)


def updateSchool():
    schoolName = input("Enter the Name for your school or 0 to quit: ")
    if schoolName == '0':
        return 0
    update_school(logged_in[0], "schoolName", schoolName)
    degree = input("Enter the degree you got from your school or 0 to quit: ")
    if degree == '0':
        return 1
    update_school(logged_in[0], "degree", degree)
    yearsAttended = input("Enter the number of years you attened the school or 0 to quit: ")
    if yearsAttended == '0':
        return 2
    update_school(logged_in[0], "yearsAttended", int(yearsAttended))

    return 3


def updateProfile():
    opt = input(
        'Enter the command number of the part to update: (1) Title, (2) Major, (3) University Name, (4) About, (5)Job1, (6) Job2, (7) Job3, (8) Education ')

    if int(opt) == 1:
        title = input("enter Title for profile or 0 to quit: ")
        if title == '0':
            return 0
        update_profile(logged_in[0], 'title', title)
    elif int(opt) == 2:
        major = input("Enter your Major or 0 to quit: ")
        if major == '0':
            return 1

        major = formatCaps(major)

        update_profile(logged_in[0], "major", major)
    elif int(opt) == 3:
        uniName = input("Enter Name of your University or 0 to quit: ")
        if uniName == '0':
            return 2

        uniName = formatCaps(uniName)

        update_profile(logged_in[0], "universityName", uniName)
    elif int(opt) == 4:
        about = input("Enter info about you or 0 to quit: ")
        if about == '0':
            return 3

        update_profile(logged_in[0], "about", about)
    elif int(opt) == 5:
        updateJobMenu(1)
    elif int(opt) == 6:
        updateJobMenu(2)
    elif int(opt) == 7:
        updateJobMenu(3)
    elif int(opt) == 8:
        updateSchool()
    else:
        printInvalidEntry()
    return 0


def editProfile():
    userName = logged_in[0]

    update = input(
        "Would you like to UPDATE or continue to CREATE profile where you left off? (Type update or create): ")
    if update == 'update':
        updateProfile()
        return 0

    if (checkTitle(userName) == False):
        title = input("enter Title for profile or 0 to quit: ")
        if title == '0':
            return 0
        update_profile(logged_in[0], 'title', title)

        major = input("Enter your Major or 0 to quit: ")
        if major == '0':
            return 1

        major = formatCaps(major)

        update_profile(logged_in[0], "major", major)

        uniName = input("Enter Name of your University or 0 to quit: ")
        if uniName == '0':
            return 2

        uniName = formatCaps(uniName)

        update_profile(logged_in[0], "universityName", uniName)

        about = input("Enter info about you or 0 to quit: ")
        if about == '0':
            return 3

        update_profile(logged_in[0], "about", about)

        jobOption = input("You can create up to three jobs, would you like to create one?\n(y or n): ")
        if jobOption == 'y':
            createJobMenu(1)
            jobOption = input("Would you like to create a second job?\n(y,n): ")
            if jobOption == 'y':
                createJobMenu(2)
                jobOption = input("Would you like to create a third job?\n(y,n): ")
                if jobOption == 'y':
                    createJobMenu(3)

        schoolOption = input("Would you like to enter a school? \n(y or n): ")
        if (schoolOption == 'y'):
            createSchoolMenu()

    elif checkMajor(userName) == False:
        major = input("Enter your Major or 0 to quit: ")
        if major == '0':
            return 1

        major = formatCaps(major)

        update_profile(logged_in[0], "major", major)

        uniName = input("Enter Name of your University or 0 to quit: ")
        if uniName == '0':
            return 2

        uniName = formatCaps(uniName)

        update_profile(logged_in[0], "universityName", uniName)

        about = input("Enter info about you or 0 to quit: ")
        if about == '0':
            return 3

        update_profile(logged_in[0], "about", about)

        jobOption = input("You can create up to three jobs, would you like to create one?\n(y or n): ")
        if jobOption == 'y':
            createJobMenu(1)
            jobOption = input("Would you like to create a second job?\n(y,n): ")
            if jobOption == 'y':
                createJobMenu(2)
                jobOption = input("Would you like to create a third job?\n(y,n): ")
                if jobOption == 'y':
                    createJobMenu(3)

        schoolOption = input("Would you like to enter a school? \n(y or n): ")
        if (schoolOption == 'y'):
            createSchoolMenu()
    elif checkUniversityName(userName) == False:
        uniName = input("Enter Name of your University or 0 to quit: ")
        if uniName == '0':
            return 2

        uniName = formatCaps(uniName)

        update_profile(logged_in[0], "universityName", uniName)

        about = input("Enter info about you or 0 to quit: ")
        if about == '0':
            return 3

        update_profile(logged_in[0], "about", about)

        jobOption = input("You can create up to three jobs, would you like to create one?\n(y or n): ")
        if jobOption == 'y':
            createJobMenu(1)
            jobOption = input("Would you like to create a second job?\n(y,n): ")
            if jobOption == 'y':
                createJobMenu(2)
                jobOption = input("Would you like to create a third job?\n(y,n): ")
                if jobOption == 'y':
                    createJobMenu(3)

        schoolOption = input("Would you like to enter a school? \n(y or n): ")
        if (schoolOption == 'y'):
            createSchoolMenu()
    elif checkAbout(userName) == False:
        about = input("Enter info about you or 0 to quit: ")
        if about == '0':
            return 3

        update_profile(logged_in[0], "about", about)

        jobOption = input("You can create up to three jobs, would you like to create one?\n(y or n): ")
        if jobOption == 'y':
            createJobMenu(1)
            jobOption = input("Would you like to create a second job?\n(y,n): ")
            if jobOption == 'y':
                createJobMenu(2)
                jobOption = input("Would you like to create a third job?\n(y,n): ")
                if jobOption == 'y':
                    createJobMenu(3)

        schoolOption = input("Would you like to enter a school? \n(y or n): ")
        if (schoolOption == 'y'):
            createSchoolMenu()
    elif checkJob(userName) == 0:
        jobOption = input("You can create up to three jobs, would you like to create one?\n(y or n): ")
        if jobOption == 'y':
            createJobMenu(1)
            jobOption = input("Would you like to create a second job?\n(y,n): ")
            if jobOption == 'y':
                createJobMenu(2)
                jobOption = input("Would you like to create a third job?\n(y,n): ")
                if jobOption == 'y':
                    createJobMenu(3)
        schoolOption = input("Would you like to enter a school? \n(y or n): ")
        if (schoolOption == 'y'):
            createSchoolMenu()
    elif checkJob(userName) == 1:
        jobOption = input("Would you like to create a second job?\n(y,n): ")
        if jobOption == 'y':
            createJobMenu(2)
            jobOption = input("Would you like to create a third job?\n(y,n): ")
            if jobOption == 'y':
                createJobMenu(3)
    elif checkJob(userName) == 2:
        jobOption = input("Would you like to create a third job?\n(y,n): ")
        if jobOption == 'y':
            createJobMenu(3)
        schoolOption = input("Would you like to enter a school? \n(y or n): ")
        if (schoolOption == 'y'):
            createSchoolMenu()
    elif checkJob(userName) == 2 and checkSchool(userName) == False:
        schoolOption = input("Would you like to enter a school? \n(y or n): ")
        if (schoolOption == 'y'):
            createSchoolMenu()

    return 0


# displays the profile of the currently logged in user
def viewProfile(username):
    profileData = getProfileInfo(username).fetchall()[0]
    accountData = getAccountInfo(username).fetchall()[0]
    jobData = getExperienceInfo(username).fetchall()
    educData = getEducationInfo(username).fetchall()
    numFriends = getNumFriends(username).fetchall()[0]

    print("\n\t\t" + accountData[2] + " " + accountData[3] + "\n")  # display the full name
    print(str(profileData[1]) + "\nMajor: " + str(profileData[2]))  # display title and major
    print("School: " + str(profileData[3]) + "\nAbout: " + str(profileData[4]) + "\n")  # display school and about
    print("Total Friends: " + str(numFriends[0]) + "\n")
    # if there is job experience, display job experience
    if (len(jobData) > 0):
        print("Experience:\n")
        for d in jobData:  # iterate through all the jobs from the database
            print("\t" + d[2] +
                  "\n\t" + d[3] +
                  "\n\tStart: " + d[4] +
                  "\n\tEnd: " + d[5] +
                  "\n\t" + d[6] +
                  "\n\t" + d[7] + "\n")

    # if there is education saved in database, display education
    if (len(educData) > 0):
        for d in educData:
            print("Education:\n" +
                  "\tSchool Name: " + d[1] +
                  "\n\tDegree: " + d[2] +
                  "\n\tYears attended: " + str(d[3]) + "\n")

    return


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def friendsMenu():
    while True:
        printFriendsMenu()

        opt = input("Enter Command: ")

        if int(opt) == 1:  # view friends list
            displayAllFriends(logged_in[0])
        elif int(opt) == 2:  # view pending friends requests
            print("Pending friend requests:\n")
            displayAllFriendRequests(logged_in[0])
        elif int(opt) == 3:  # add a friend
            addFriendMenu(logged_in[0])
        elif int(opt) == 4:  # remove a friend
            removeFriendMenu(logged_in[0])
        elif int(opt) == 5:  # view a friend's profile
            displayFriendsWithProfile(logged_in[0])
        else:
            break
    return 1


# displays all the friends of the current user (even those without profiles)
def displayAllFriends(currUser):
    print("\nFriends list:")
    friends = findFriends(currUser)
    if len(friends) > 0:
        i = 1
        for f in findFriends(currUser):
            print(str(i) + ". " + f[1] + " " + f[2] + " (" + f[0] + ")")
            i += 1
        print("\n")
        return 1
    else:
        print("You don't have any friends!\n")
    return None


# displays all the friends of the current user (does not include those without profiles)
def displayFriendsWithProfile(username):
    print("\nFriends with profiles: ")
    friends = getFriendsWithProfile(username).fetchall()
    if len(friends) > 0:
        for r in getFriendsWithProfile(username):
             print(r[1] + " " + r[2] + " (" + r[0] + ")\n")
        toView = input("Enter the username of the friend whose profile you want to view: ")
        viewProfile(toView)  # view the profile of the entered username
        return 1
    else:
        print("None of your friends have a profile!\n")
    return None


# menu to display when the user wants to add a friend
def addFriendMenu(username):
    toAdd = input("Enter username of friend to add (0 to cancel adding a friend): ")

    if toAdd != '0':
        # rowcount == -1 means empty cursor, query did not return anything
        if len(findSpecificFriend(username, toAdd).fetchall()) == 0:
            displayUserInfo(toAdd)  # displays basic info (name, username, major, university) of the user to be added
            if input("Would you like to send a friend request to " + toAdd + "? (Y/N) ") == 'Y':
                if requestFriend(toAdd, logged_in[0]) == 3:
                    print("You succesfully sent a friend request to " + toAdd + ".\n")
                    return True
                else:
                    print("You already sent a friend request to " + toAdd + ".\n")
                    return False
            else:
                return False
        else:
            print("\nYou and " + toAdd + " are already friends!\n")
    return None


# displays all the pending friend request for the specified username
def displayAllFriendRequests(username):
    requests = getAllFriendRequests(username).fetchall()  # gets all pending friend request of the current user
    if len(requests) > 0:
        for r in requests:  # iterate through friend requests and ask user if they want to accept, reject, or cancel
            print(r[2] + " " + r[3] + " (" + r[1] + ") wants to be your friend! ")
            opt = input("Enter A to Accept, R to Reject, or C to Cancel: ")
            if opt == 'A' or opt == 'a':  # user accepts a friend request
                if acceptRequest(username, r[1]) != 0:
                    print("\nYou have accepted " + r[1] + "'s friend request!")
            elif opt == 'R' or opt == 'r':  # user rejects a friend request
                if rejectRequest(username, r[1]) != 0:
                    print("\nYou have rejected " + r[1] + "'s friend request!")
            else:  # cancel to stop accepting friend requests
                break
    else:
        print("You don't have any friend requests.\n")
    return None


# menu for removing a friend
def removeFriendMenu(username):
    if displayAllFriends(username) != None:
        removedFriend = input("Enter the username of the friend you would like to remove (0 to cancel): ")
        if removedFriend != '0':
            if removeFriend(username, removedFriend) == 1:
                print("Succesfully removed " + removedFriend + " from your friends list.\n")
                return 1
    return None

# view all the job titles in the system
def viewJobTitles():
    print("\nAll job titles currently in InCollege:\n")
    jobs = getAllJobTitles()  # retrieve all the existing job titles in the system

    # display the jobs
    count = 1
    for t in jobs:
        print(str(count) + ". " + t[1])
        count+=1

    toView = input("\nEnter the number of the job you want to view (0 to cancel): ")
    if toView == "0":
        return None
    else:
        printJobDetails(jobs[int(toView)-1][0])   # print job details for the user
        jobOptions(logged_in[0], jobs[int(toView)-1][0])  # ask the user what to do
        return True


# function to print the details of the specified job
def printJobDetails(jobID):
    j = getJobDetails(jobID)  # retrieve details from database

    print("\nTitle: " + j[1] + "\nEmployer: " + j[3] + "\nLocation: " + j[4] + "\nSalary: " + j[5] + "\nDescription: " +
          j[2] + "\n")

    return None


# asks the user what they want to do with a selected job
def jobOptions(user, jobID):
    printJobOptionsMenu()
    option = input("Enter command: ")

    if option == "1":  # user wants to apply for the job
        if apply_job(getJobDetails(jobID), user, logged_in[2], logged_in[3]):
            print("You have sucessfully submitted your application!\n")
    elif option == "2":  # user wants to save the job
        if saveJob(user, jobID):
            print("\nSuccessfully saved job!")
            return True
        else:
            print("\nYou have already saved this job!")
            return False
    else:
        return None

# displays all the jobs posted by the given first name and last name
def viewAllPostedJobs(firstname, lastname):
    print("\nJobs you have posted:\n")

    jobs = getJobsByPoster(firstname, lastname)  # get all the jobs posted by the currently logged in user

    if len(jobs) == 0:
        print("\nYou haven't posted any jobs!")
        return None

    count = 1

    # display all the jobs posted by currently logged in user
    for j in jobs:
        print(str(count) + ".  Title: " + j[1] + "\n\tEmployer: " + j[3] + "\n\tLocation: " + j[4] + "\n\tSalary: " + j[
            5] + "\n\tDescription: " + j[2] + "\n")
        count += 1


# delete a job the user posted
def deleteJobMenu(firstname, lastname):
    jobs = getJobsByPoster(firstname, lastname)  # get all the jobs posted by the currently logged in user

    toDelete = input("Enter the number of the job you want to delete (0 to cancel): ")

    if toDelete == "0":  # user cancels
        return None
    else:
        deleteJob(jobs[int(toDelete)-1][0])  # delete the jobs + set the applications associated to it as deleted + delete items from
        print("\nSuccessfully deleted job!\n")
        return True


# prints all the saved jobs of the current user
def viewSavedJobs(user):
    print("\nYour saved jobs: \n")

    jobs = getAllSavedJobs(user)  # retrieve all the jobs saved by the user from the database

    if(len(jobs) == 0):
        print("You don't have any jobs saved!\n")
        return None

    # display all the jobs saved by the user
    count = 1
    for j in jobs:
        print(str(count) + ".  Title: " + j[1] +
              "\n\tEmployer: " + j[3] +
              "\n\tLocation: " + j[4] +
              "\n\tSalary: " + j[5] +
              "\n\tDescription: " + j[2] + "\n")
        count += 1

    toModify = input("Enter the number of the job you want to modify (0 to cancel): ")

    if toModify == "0":
        return None
    else:
        printJobDetails(jobs[int(toModify) - 1][0])  # print the details of the job they want to modify
        savedJobOptions(user, jobs[int(toModify)-1][0])
        return True


# options when a user views a job in his saved jobs list
def savedJobOptions(user, jobID):
    printSavedJobOptionsMenu()
    option = input("Enter command: ")

    if option == "1":  # user wants to apply for the job
        if apply_job(getJobDetails(jobID), user, logged_in[2], logged_in[3]):
            print("You have sucessfully submitted your application!\n")
            removeFromSavedJobs(user, jobID)
    elif option == "2":  # user wants to remove the job from their saved list
        if removeFromSavedJobs(user, jobID):
            print("\nSuccessfully removed job!")
            return True
    else:
        return None


# checks if any of the applications the user submitted has been deleted.
def checkDeletedApplications(user):
    a = getDeletedApplications(user)
    if len(a) != 0:
        return True
    return False


# displasy all the job titles of the jobs the currently logged in user has applied for
def displayAllJobTitlesAppliedFor(user):
    print("\nJobs you have applied for:\n")

    jobs = getAllJobTitlesAppliedFor(user)

    if len(jobs) == 0:
        print("You have not applied for a job!\n")
        return False

    count = 1
    for r in jobs:
        print(str(count) + ". " + r[1])
        count+=1

    return None