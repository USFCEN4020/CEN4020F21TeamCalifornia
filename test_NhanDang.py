import pytest
import main

@pytest.mark.parametrize("username, password",
                         [ ("nhandang", "@Pass"),
                           ("abcd", "1234")

                         ]
                         )
def test_login(username, password):
    assert main.find_account(username,password), "Logined Successfully"

def test_passCheck():
    # test all invalid pass=>should return val = false
    error = ""
    val = True
    error += "ERROR: Minimum 8 characters" if main.password_check("dsa123") == False else error
    error += "ERROR: Maximum 12 characters" if main.password_check("sfsdgadghfhs46sdfss345654") == False else error
    error += "ERROR: At least one capital letter" if main.password_check("abcdsrfv1") == False else error
    error += "ERROR: At least 1 digit" if main.password_check("@abcderfgh") == False else error
    error += "ERROR: At least one non-alpha character" if main.password_check("abcdgks123") == False else error

    val = False if main.password_check("dsa123") == False else val
    val = False if main.password_check("sfsdgadghfhs46sdfss345654") == False else val
    val = False if main.password_check("abcdsrfv1") == False else val
    val = False if main.password_check("abcderfgh") == False else val
    val = False if main.password_check("abcdgks123") == False else val

    assert val == False, error



