import sys
import io
from typing import NoReturn
import pytest
from pytest_mock import mocker
sys.path.insert(0,'InCollege Code')
import menus
import messages
import verify_acc


#tests for stories 4,5,6 on epic 1

def test_Main_Menu():
    sys.stdin = io.StringIO('0')
    assert menus.mainMenu() == 0

def test_findJob():
    sys.stdin = io.StringIO('1 \n 0\n')
    assert menus.mainMenu() == 0
#Test Depricated
# def test_findSomeone():
#     sys.stdin = io.StringIO('1 \n 0\n')
#     assert menus.mainMenu() == 0

def test_skillsMenu():
    sys.stdin = io.StringIO('3 \n 1\n2\n3\n4\n5\n0\n0\n')
    assert menus.mainMenu() == 0   

#test for new stoies  1, , on Epic 2

def test_studentSuccessStory():
    assert messages.printStudentSuccess() == 0

def test_viewVideo():
    sys.stdin = io.StringIO('3\n0')
    assert menus.homeMenu() == None



