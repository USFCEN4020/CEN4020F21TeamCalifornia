import sys
import io
from typing import NoReturn
import pytest
from pytest_mock import mocker
import sqlite3
#sys.path.insert(0,'InCollege Code')
import menus
import messages
import verify_acc
import search


#tests for stories 4,5,6 on epic 1

def test_Main_Menu():
    sys.stdin = io.StringIO('0')
    assert menus.mainMenu() == 0
#Test Depricated
# def test_findJob():
#     sys.stdin = io.StringIO('1 \n 0\n')
#     assert menus.mainMenu() == 0
#Test Depricated
# def test_findSomeone():
#     sys.stdin = io.StringIO('1 \n 0\n')
#     assert menus.mainMenu() == 0

def test_skillsMenu():
    sys.stdin = io.StringIO('4\n1\n2\n3\n4\n5\n0\n0\n')
    assert menus.mainMenu() == 0   

#test for new stoies  1, , on Epic 2

def test_studentSuccessStory():
    assert messages.printStudentSuccess() == 0

def test_viewVideo():
    sys.stdin = io.StringIO('4\n0')
    assert menus.homeMenu() == None

def test_CreateAccount():
    conn = sqlite3.connect('Accounts.db')
    c = conn.cursor()   
    for row in c.execute("""SELECT * FROM Accounts"""):
        assert(search.find_user(row[2],row[3])) == True
    assert search.find_user("fake","person") == False




