#imports all functions from messages.py
from messages import *
#imports all functions from search.py
from search import *
#imports all functions from jobs.py
from jobs import *
#imports all functions from update_acc.py
from update_acc import *
#imports all functions from personalProfile.py
from personalProfile import *

logged_in = []

#/////////////////////////////////////////////////////////////////////////     LOGIN MENU     /////////////////////////////////////////////////////////////////////////

def loginMenu():
    
    print("\nLog In to InCollege\n")
    
    create_table()
    
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
    #gets the first and last name of the current user that is logged in
    logged_in = current_user(username, password)
    mainMenu()



#/////////////////////////////////////////////////////////////////////////     HOME MENU     /////////////////////////////////////////////////////////////////////////

def homeMenu():
    
    print("Welcome to InCollege.")
    #prints the student success story found on messages.py
    printStudentSuccess()
    
    #Creates a database for the profiles if one doesnt exisit
    create_profile_table()
    
    while True:   
        #prints the home menu
        printHomeMenu()
        
        #gets user input
        select = input("Enter command: ")

        if(select == "1" or select == "2" or select == "3" or select == "4" or select == "0"or select == "5"or select == "6"):
            break
        else:
            #if user inputs an incorrect value an this function prints an error message
            printInvalidEntry()
            continue

    if(select == "1"):
        loginMenu()
    elif(select == "2"):
        createAccountMenu()
    elif(select == "3"):
        searchPeople()
    elif(select == "4"):
        print("\nVideo is now playing...\n")
    elif (select == "5"):
        usefulLinksMenu()
    elif (select == "6"):
        impLinksMenu()
    elif(select == "0"):
        print("Thank you for using InCollege!")
        quit()
    else:
        printInvalidEntry()


#/////////////////////////////////////////////////////////////////////     CREATE ACCOUNT MENU     ////////////////////////////////////////////////////////////////////

def createAccountMenu():
    
    print("\nCreate a New Account\n")

    create_table()

    if number_rows() < 5:
        username = input("Enter username: ")
        password = input("Enter password: ")
        firstname = input("Enter First Name: ")
        lastname = input("Enter Last Name: ")

        # check if username is unique and password is valid
        if not unique_user(username) and password_check(password):
            data_entry(username, password,firstname,lastname,1,1,1,"English")
            print("Successfully created an account\n")
    else:
        print("All permitted accounts have been created, please come back later\n")
    return 0

#/////////////////////////////////////////////////////////////////////////     MAIN MENU     /////////////////////////////////////////////////////////////////////////

def mainMenu():
    
    while True:
        global logged_in
        #prints the main menu
        printMainMenu(logged_in[0])
        #gets user input
        opt = input("Enter command: ")

        if int(opt) == 1: #search for job
            jobMenu()
        elif int(opt) == 2:  
            searchPeople()
        elif int(opt) == 3:  # learn a new skill
            skillMenu()
        elif int(opt) == 4:
            usefulLinksMenu()
        elif int(opt) == 5:
            impLinksMenu()
        elif int(opt) == 6:
            if hasProfile(logged_in[0]):
                #update/edit profile Function goes here
                None # temp value for code to work
            else:
                #Creates profile if one does not exist.
                createProfileMenu()
        elif int(opt) == 0:
            
            logged_in = []
            print("You have sucessfully logged out!\n")
            break
        else:
            printInvalidEntry()
    return 0

#/////////////////////////////////////////////////////////////////////////     SKILL MENU     /////////////////////////////////////////////////////////////////////////

def skillMenu():
    
    while True:
        #prints the list of skills
        printSkillList()
        #gets user input
        skill = input("Select a skill: ")
    
        if skill != "0":
            #prints an under construction message
            printUnderConstruction()
        elif skill == "0":
            break
        else:
            printInvalidEntry()
    return 0

#/////////////////////////////////////////////////////////////////////////     JOB MENU     ///////////////////////////////////////////////////////////////////////////

def jobMenu():
    
    while True:
        print("\nJob search/internship.\n")

        printJobMenu()
        #creates a database for jobs if one doesnt exist.
        create_job_table()

        select = input("Enter Command: ")

        if select == "1":
            postJob(logged_in[2], logged_in[3])
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
            print("In College: Welcome to In College, the world's largest college student network with many users in many countries and territories worldwide\n")
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
            print("In College: Welcome to In College, the world's largest college student network with many users in many countries and territories worldwide")
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

#/////////////////////////////////////////////////////////////////////////////     Create Job Menu     //////////////////////////////////////////////////////////////////

def createJobMenu(jobId):
    create_job(logged_in,jobId)

    title = input("enter Title for profile or 0 to quit: ")
    if title == '0':
        return 0
    update_job(logged_in[0],jobId,'title',title)

    employer = input("Enter your employer or 0 to quit: ")
    if employer == '0':
        return 1
    
    update_job(logged_in[0],jobId,"employer",employer)

    dateStart = input("Enter the Date you started the job or 0 to quit: ")
    if dateStart == '0':
        return 2

    update_job(logged_in[0],jobId,'dateStart',dateStart)

    dateEnd = input("Enter the Date you ended the job or 0 to quit: ")
    if dateEnd == '0':
        return 3

    update_job(logged_in[0],jobId,'dateEnd',dateEnd)

    location = input("Enter the location of the job or 0 to quit: ")
    if location == '0':
        return 4
    update_job(logged_in[0],jobId,'location',location)
    
    description = input("Enter a description for the job or 0 to quit: ")
    if description == '0':
        return 2
    
    update_job(logged_in[0],jobId,'description',description)


#/////////////////////////////////////////////////////////////////////////////////////   Create School Menu   /////////////////////////////////////////////////////////////

def createSchoolMenu():
    create_school(logged_in[0])
    schoolName = input("Enter the Name for your school or 0 to quit: ")
    if schoolName == '0':
        return 0
    update_school(logged_in[0],"schoolName",schoolName)
    degree = input("Enter the degree you got from your school or 0 to quit: ")
    if degree == '0':
        return 1
    update_school(logged_in[0],"degree",degree)
    yearsAttended = input("Enter the number of years you attened the school or 0 to quit: ")
    if yearsAttended == '0':
        return 2
    update_school(logged_in[0],"yearsAttended",int(yearsAttended))
    
    return 3


#///////////////////////////////////////////////////////////////////////////////////////    Create Profile Menu    ///////////////////////////////////////////////////////

def createProfileMenu():
    create_profile(logged_in[0])
    
    title = input("enter Title for profile or 0 to quit: ")
    if title == '0':
        return 0
    update_profile(logged_in[0],'title',title)

    major = input("Enter your Major or 0 to quit: ")
    if major == '0':
        return 1
    
    major = formatCaps(major)

    update_profile(logged_in[0],"major",major)

    uniName = input("Enter Name of your University or 0 to quit: ")
    if uniName == '0':
        update_profile(title,major,None,None)
        return 2

    uniName = formatCaps(uniName)

    update_profile(logged_in[0],"universityName",uniName)

    about = input("Enter info about you or 0 to quit: ")
    if about == '0':
        
        return 3 

    update_profile(logged_in[0],"about",about)

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
    if(schoolOption == 'y'):
        createSchoolMenu()
    return 4

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////




