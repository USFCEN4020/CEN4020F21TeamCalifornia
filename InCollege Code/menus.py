#imports all functions from messages.py
from messages import *
#imports all functions from verify_acc.py
from verify_acc import *

global logged_in


def homeMenu():
    
    print("Welcome to InCollege.")
    #prints the student success story found on messages.py
    printStudentSuccess()
    
    while True:   
        #prints the home menu
        printHomeMenu()
        #gets user input
        select = input("Enter command: ")

        if(select == "1" or select == "2" or select == "3" or select == "0"):
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
        print("\nVideo is now playing...\n")
    elif(select == "0"):
        print("Thank you for using InCollege!")
        quit()





def loginMenu():
    
    print("\nLog In to InCollege\n")

    found = False

    while not found:  # continue looping as long as user inputs invalid login info
        # get input from the user
        username = input("Enter username: ")
        password = input("Enter password: ")

        # check if username and password are valid
        found = find_account(username, password)
        if not found:
            print("Incorrect username/password, please try again\n")
    print("\nYou have successfully logged in\n")
    logged_in = True
    mainMenu()





def createAccountMenu():
    
    print("\nCreate a New Account\n")

    # read CSV file containing all account information
    accounts = pd.read_csv('accounts.csv', index_col=0, squeeze=True, header=None).to_dict()

    # TODO: looping while user inputs invalid values
    if len(accounts.keys()) < 5:
        username = input("Enter username: ")
        password = input("Enter password: ")

        # check if username is unique and password is valid
        if not username in accounts and password_check(password):
            accounts[username] = password  # add <username, password> pair into dict
            print("Successfully created an account\n")
    else:
        print("All permitted accounts have been created, please come back later\n")

    # save accounts dict into CSV file
    df = pd.DataFrame(accounts.items())
    df.to_csv('accounts.csv', index=False, header=False)
    return 0





def mainMenu():
    
    while True:
        #prints the main menu
        printMainMenu()
        #gets user input
        opt = input("Enter command: ")

        if int(opt) == 1: #search for job
            #prints an under construction message
            printUnderConstruction()
        elif int(opt) == 2:  
            searchPeople()
        elif int(opt) == 3:  # learn a new skill
            skillMenu()
        else:
            logged_in = False
            print("You have sucessfully logged out!\n")
            break
    return 0





def skillMenu():
    
    while True:
        #prints the list of skills
        printSkillList()
        #gets user input
        skill = input("Select a skill: ")
    
        if skill != "0":
            #prints an under construction message
            printUnderConstruction()
        else:
            break
    return 0





def searchPeople():
    print("\nSearch For A Person.\n")

    print("Please enter the first and last name of the person you wish to search for.\n")

    firstName = input("Enter first name: ")
    lastName = input("Enter last name: ")

    print(firstName, lastName)

    return
