import pandas as pd

# This function looks for the given username and password in the CSV file
def find_account(findUsername, findPassword):
    # get all the accounts from the csv file
    accounts = pd.read_csv('accounts.csv', index_col=0, squeeze=True, header=None).to_dict()

    # initialize temp values to False
    un = False
    pw = False

    # look for username in accounts dict
    for u in accounts.keys():
        if u == findUsername:
            un = True  # change value of un to True if found

    # look for password in accounts dict
    for p in accounts.values():
        if p == findPassword:
            pw = True  # change value of pw to True if found

    return pw and un





# Function to validate the password
def password_check(passwd):
    # declaring the special characters to be used to enter by user

    SpecialSym = ['$', '@', '#', '%']

    # variable used to determine the valid characters within the loop
    val = True

    # beginning of the loop

    # checks the minimum length validation
    if len(passwd) < 8:
        print('length should be at least 8')
        val = False

    # checks the max length validation
    if len(passwd) > 12:
        print('length should be not be greater than 12')
        val = False

    # checks for 1 digit input
    if not any(char.isdigit() for char in passwd):
        print('Password should have at least one digit')
        val = False

    # checks for Upper case input
    if not any(char.isupper() for char in passwd):
        print('Password should have at least one uppercase letter')
        val = False

    # checks for special synbol inout
    if not any(char in SpecialSym for char in passwd):
        print('Password should have at least one of the symbols $@#')
        val = False

    # # checks if inputs are valid
    # if val:
    #     return val
    return val
