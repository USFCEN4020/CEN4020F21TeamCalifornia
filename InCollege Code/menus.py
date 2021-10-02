#imports all functions from messages.py
from messages import *
#imports all functions from search.py
from search import *
#imports all functions from jobs.py
from jobs import *
#imports all functions from update_acc.py
from update_acc import *

logged_in = []

#/////////////////////////////////////////////////////////////////////////     HOME MENU     /////////////////////////////////////////////////////////////////////////

def homeMenu():
    
    print("Welcome to InCollege.")
    #prints the student success story found on messages.py
    printStudentSuccess()
    
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
        #prints the main menu
        printMainMenu()
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
        elif int(opt) == 0:
            global logged_in
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
            printUnderConstruction()
        elif int(opt) == 3:
            printUnderConstruction()
        elif int(opt) == 4:
            printUnderConstruction()
        elif int(opt) == 5:
            privacyPolicyMenu()
        elif int(opt) == 6:
            printUnderConstruction()
        elif int(opt) == 7:
            printUnderConstruction()
        elif int(opt) == 8:
            printUnderConstruction()
        elif int(opt) == 9:
            guestControlMenu()
        elif int(opt) == 10:
            printUnderConstruction() #languages menu
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
            print( "In College Pressroom: Stay on top of the latest news, updates, and reports")
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
                update_lang_option(logged_in[0], logged_in[1])
            elif int(opt) == 0:
                break
            else:
                printInvalidEntry()
    return

# /////////////////////////////////////////////////////////////////////////     LANGUAGE MENU     //////////////////////////////////////////////////////////////////////////

def languageMenu():
    while True:
        printLanguageMenu()

        # gets user input
        opt = input("Enter command: ")

        if int(opt) == 1:
            update_lang_option(logged_in[0], logged_in[1])
        elif int(opt) == 2:
            break
    return

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
