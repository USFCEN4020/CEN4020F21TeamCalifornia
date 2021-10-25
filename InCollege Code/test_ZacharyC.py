import sqlite3
import pytest
import io
import personalProfile
import menus
import verify_acc
import search


#this function tests if you can create up to and no more than 10 accounts
def test_maximum_num_accounts():
    
    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    #Creates a database for the profiles if one doesnt exisit
    verify_acc.create_tables()
    
    #creates 10 user accounts
    verify_acc.data_entry("zchenoweth", "Chenoweth1@", "Zachary", "Chenoweth", 1, 1, 1, "English")
    verify_acc.data_entry("CoolDude123", "CoolDude1@", "John", "Smith", 1, 1, 1, "English")
    verify_acc.data_entry("tester123", "Tester123@", "Anna", "Collins", 1, 1, 1, "English")
    verify_acc.data_entry("Coder321", "Coder321@", "Henry", "Potter", 1, 1, 1, "English")
    verify_acc.data_entry("princess123", "Princess1@", "Lucy", "Johnson", 1, 1, 1, "English")
    verify_acc.data_entry("kingofpop1", "Hehe1234@", "Michael", "Jackson", 1, 1, 1, "English")
    verify_acc.data_entry("metalhead123", "Metallica1@", "James", "Hetfield", 1, 1, 1, "English")
    verify_acc.data_entry("Sweetypie", "Sweetpie1@", "Mary", "Noname", 1, 1, 1, "English")
    verify_acc.data_entry("fakeperson", "Fake1234@", "Fake", "Person", 1, 1, 1, "English")
    verify_acc.data_entry("Noideas123", "Noideas1@", "Larry", "Mason", 1, 1, 1, "English")

    print("Test to add 11th account(should print all accounts are full):")
    #should print that accounts are all full
    assert menus.createAccountMenu() == 0

    return



#This function tests if a profile database is created and if a Student can create a profile and add it to the database
def test_create_profile():

    conn = sqlite3.connect('InCollege.db')
    c = conn.cursor()

    #create the database if it doesnt already exist
    verify_acc.create_tables()
    #creates a new profile and stores it in the database
    personalProfile.create_profile("CoolDude123")

    # display contents of db before signing up
    for r in c.execute("SELECT * FROM personalProfile"):
        print(r)

    #creates a new profile and stores it in the database
    personalProfile.create_profile("metalhead123")
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



# this function test the search for a person functionality
def test_searchPeople(monkeypatch):
    #search by last name
    input = 'Chenoweth\n'
    monkeypatch.setattr('sys.stdin', io.StringIO(input))
    assert search.searchPeople("kingofpop1") == True

    #search by major
    input = 'Computer Engineering\n'
    monkeypatch.setattr('sys.stdin', io.StringIO(input))
    assert search.searchPeople("kingofpop1") == True

    #search by university
    input = 'University of South Florida\n'
    monkeypatch.setattr('sys.stdin', io.StringIO(input))
    assert search.searchPeople("kingofpop1") == True

    #no matching result
    input = 'Computer Science\n'
    monkeypatch.setattr('sys.stdin', io.StringIO(input))
    assert search.searchPeople("kingofpop1") == False

    return



# this function tests to see if the show my network menu appears properly
def test_show_my_network(monkeypatch):
    input = '0\n'
    monkeypatch.setattr('sys.stdin', io.StringIO(input))
    assert menus.friendsMenu() == 1
    return
