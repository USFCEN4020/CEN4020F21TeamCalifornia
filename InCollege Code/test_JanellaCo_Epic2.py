import sqlite3
import pytest
import io
import menus
import jobs

# test for Requirement # 4
def test_createAccount(monkeypatch):
    # input order: Username, Password, First Name, Last Name,

    # check if user can log in right after registering
    input = 'johndoe\np@ssw0rD\nJohn\nDoe\n'
    monkeypatch.setattr('sys.stdin', io.StringIO(input))
    assert menus.createAccountMenu() == 0

def test_postJob(monkeypatch):
    # input order:
    #   Job title, Job description, Employer name, Location, Salary
    #   Return to main menu (0), Logout (0), Exit (0)

    input = '1\njohndoe\np@ssw0rD\n' \
            '1\n1\nSoftware Engineer\nSoftware Engineer\nInCollege\nFlorida\n$30,000\n' \
            '0\n0\n0\n'
    monkeypatch.setattr('sys.stdin', io.StringIO(input))
    assert menus.homeMenu() == None

def test_checkJobs():
    assert jobs.job_created() != None


