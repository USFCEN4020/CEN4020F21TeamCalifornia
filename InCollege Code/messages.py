from personalProfile import *

#/////////////////////////////////////////////////////////////////////////     PRINT SUCCESS STORY     /////////////////////////////////////////////////////////////////////////

def printStudentSuccess():
    print("\nInCollege is an amazing way to learn skills and search for a job.\n" 
          "Being a college student, I struggled to find a job in my field that I was interested in and worked well with my school schedule.\n"
          "However, after signing up with InCollege I was able to find the job of my dreams and learn some very valuable skills along the way.\n"
          "I highly recommend InCollege to anyone who is searching for a job, wants to learn new skills, or meet some amazing people.\n"
          "\n - John Smith.\n")
    return 0

#/////////////////////////////////////////////////////////////////////////     PRINT HOME MENU     ////////////////////////////////////////////////////////////////////////////

def printHomeMenu():
    print("(1) Login\n"
          "(2) Register\n"
          "(3) Find A Person\n"
          "(4) View Video\n"
          "(5) Useful Links Menu\n"
          "(6) InCollege Important Links Menu\n"
          "(0) Exit\n")
    return 0

#/////////////////////////////////////////////////////////////////////////     PRINT INVALID ENTRY     ////////////////////////////////////////////////////////////////////////

def printInvalidEntry():
    print("\nINVALID ENTRY PLEASE TRY AGAIN.\n")

#/////////////////////////////////////////////////////////////////////////     PRINT UNDER CONSTRUCTION     ///////////////////////////////////////////////////////////////////

def printUnderConstruction():
    print("\nUnder Construction...\n")
    return 0

#/////////////////////////////////////////////////////////////////////////     PRINT MAIN MENU    /////////////////////////////////////////////////////////////////////////////

def printMainMenu(userName):
    if hasProfile(userName):
        print("InCollege Main Menu\n"
            "(1) Job search / internship\n"
            "(2) Find someone you know\n"
            "(3) Learn a new skill\n"
            "(4) Useful Links\n"
            "(5) Important Links\n"
            "(6)Edit Personal Profile"
            "(0) Logout\n")
    else:
        print("InCollege Main Menu\n"
            "(1) Job search / internship\n"
            "(2) Find someone you know\n"
            "(3) Learn a new skill\n"
            "(4) Useful Links\n"
            "(5) Important Links\n"
            "(6)Create Personal Profile\n"
            "(0) Logout\n")
    return 0

#/////////////////////////////////////////////////////////////////////////     PRINT SKILL LIST     ///////////////////////////////////////////////////////////////////////////

def printSkillList():
    
    print("Skill list: ")  # tentative skill list
    
    print("(1) Python Programming\n"
          "(2) Java Programming\n"
          "(3) C++ Programming\n"
          "(4) Time Management\n"
          "(5) Effective communication\n"
          "(0) Return to Previous Menu\n")
    return 0

#/////////////////////////////////////////////////////////////////////////     PRINT JOB MENU     /////////////////////////////////////////////////////////////////////////////

def printJobMenu():
    
    print("(1) Post a job.\n"
          "(0) Return to Previous Menu.\n"  )
    return 0

#/////////////////////////////////////////////////////////////////////////     PRINT IMPORTANT LINKS MENU     ///////////////////////////////////////////////////////////////////

def printImpLinksMenu():

    print("InCollege Important Links Menu\n"
          "(1) A Copyright Notice\n"
          "(2) About\n"
          "(3) Accessibility\n"
          "(4) User Agreement\n"
          "(5) Privacy Policy\n"
          "(6) Cookie Policy\n"
          "(7) Copyright Policy\n"
          "(8) Brand Policy\n"
          "(9) Guest Controls\n"
          "(10) Languages\n"
          "(0) Return to Previous Menu\n")
    return

#/////////////////////////////////////////////////////////////////////////     PRINT USEFUL LINKS MENU     ///////////////////////////////////////////////////////////////////

def printUsefulLinksMenu():
    
    print("Useful Links Menu\n"
          "(1) General\n"
          "(2) Browse InCollege\n"
          "(3) Business Solutions\n"
          "(4) Directories\n"
          "(0) Return to Previous Menu\n")

    return

#/////////////////////////////////////////////////////////////////////////     PRINT USEFUL GENERAL MENU     ///////////////////////////////////////////////////////////////////

def printUsefulGeneralGroup():
    
    print("Useful Links Menu\n"
          "(1) Sign Up\n"
          "(2) Help Center\n"
          "(3) About\n"
          "(4) Press\n"
          "(5) Blog\n"
          "(6) Careers\n"
          "(7) Developers\n"
          "(0) Return to Previous Menu\n")
    return

#/////////////////////////////////////////////////////////////////////////     PRINT GUEST CONTROL MENU     //////////////////////////////////////////////////////////////////////

def printGuestControlMenu():
    
    print("Guest Control Menu\n"
          "(1) Turn ON/OFF Email\n"
          "(2) Turn ON/OFF SMS\n"
          "(3) Turn ON/OFF Ads\n"
          "(4) Change Language\n"
          "(0) Return to Previous Menu\n")
    return

#/////////////////////////////////////////////////////////////////////////     PRINT LANGUAGE MENU     //////////////////////////////////////////////////////////////////////////

def printLanguageMenu():
    
    print("Language Menu\n"
          "(1) Change Language to English\n"
          "(2) Change Language to Spanish\n"
          "(0) Return to Previous Menu\n")
    return

#/////////////////////////////////////////////////////////////////////////     PRINT PRIVACY POLICY MENU     ////////////////////////////////////////////////////////////////////


def printPrivacyPolicyMenu():
    
    print("Privacy Policy Menu\n"
          "(1) View Privacy Policy\n"
          "(2) Guest Controls\n"
          "(0) Return to Previous Menu\n")
    return
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
