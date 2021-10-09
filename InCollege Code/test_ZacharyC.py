import sqlite3
import pytest
import io
import personalProfile

#This function tests if a profile database is created and if a Student can create a profile and add it to the database
def test_create_profile():

    conn = sqlite3.connect('personalProfile.db')
    c = conn.cursor()

    #create the database if it doesnt already exist
    personalProfile.create_profile_table()
    #creates a new profile and stores it in the database
    personalProfile.create_profile("coolDude123")

    # display contents of db before signing up
    for r in c.execute("SELECT * FROM personalProfile"):
        print(r)

    #creates a new profile and stores it in the database
    personalProfile.create_profile("zchenoweth")
    print("\n")
    # display contents of db after signing up
    for r in c.execute("SELECT * FROM personalProfile"):
        print(r)
    return



#This function tests if the format for major and university name meets the specified requirements 
def test_formatCaps():
    assert personalProfile.formatCaps("hEllO WoRLD!!!") == "Hello World!!!"
    assert personalProfile.formatCaps("hEllO") == "Hello"
    assert personalProfile.formatCaps("This is A test") == "This Is A Test"
    return


#test_create_profile()
#test_formatCaps()