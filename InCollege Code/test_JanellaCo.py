import sqlite3
import pytest
import io

import menus

# testing option 6 - Important Links Menu when not logged in
def test_impLinks(monkeypatch):
    # string that simulates input
    input = '1\n0\n2\n3\n4\n5\n' \
            '1\n2\n0\n' \
            '6\n7\n8\n' \
            '9\n10\n0\n'

    # attach the input string to the stdin of the program
    monkeypatch.setattr('sys.stdin', io.StringIO(input))

    # run the function we want to test and check output value
    assert menus.impLinksMenu() == 0

def test_usefulLinks(monkeypatch):
    input='2\n3\n4\n1\n0\n0\n'

    monkeypatch.setattr('sys.stdin', io.StringIO(input))

    assert menus.usefulLinksMenu() == 0

def test_usefulGeneralGroup(monkeypatch):
    input = '2\n3\n4\n5\n6\n7\n0\n'

    monkeypatch.setattr('sys.stdin', io.StringIO(input))

    assert menus.usefulGeneralGroup() == 0


# test for creating an account
# When a user signs up, Email, SMS, and Targeted are all set 1 or True, Language is set to "English", and Stored in DB
def test_createAccount(monkeypatch):

    conn = sqlite3.connect('Accounts.db')
    c = conn.cursor()
    # display contents of db before signing up
    for r in c.execute("SELECT * FROM Accounts"):
        print(r)

    input = 'johndoe\np@ssw0rD\nJohn\nDoe\n0\n0\n0'

    monkeypatch.setattr('sys.stdin', io.StringIO(input))

    assert menus.createAccountMenu() == 0

    # display contents of db after signing up
    for r in c.execute("SELECT * FROM Accounts"):
        print(r)