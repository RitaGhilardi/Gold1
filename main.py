import argparse

from packages.log_in import log_in
from packages.add_employee import add_employee
from packages.add_user import add_user
from packages.buy_metals import buy_metal
from packages.pay_loan import pay_loan
from packages.read_register import read_register
from packages.get_balance import get_balance
from packages.check_password import check_password
from packages.get_number import get_number
from packages.get_date import get_date
from packages.get_cvc import get_cvc
from packages.check_cvc import ask_cvc
from packages.verify_user import verify_user


def parse_arguments():

    parser = argparse.ArgumentParser()

    parser.add_argument("username", help="Insert the username that"
                        "you want to use", default=None)

    parser.add_argument("password", help="Insert the password that"
                        "you want to use", default=None)

    parser.add_argument("-au", "--add_user",
                        help="Register as a user with the username and"
                        "password that you provide", action="store_true",
                        default=False)

    parser.add_argument("-ae", "--add_employee",
                        help="Register as an employee with the username and"
                        "password that you provide", action="store_true",
                        default=False)

    parser.add_argument("-bm", "--buy_metal", default=None,
                        help="Specify the metal that you want to buy."
                        "The metals that we trade are Gold, Silver, Palladium,"
                        "Platinum, Rhodium. (this argument must be"
                        "used with bq) ", type=str,
                        choices=["Gold", "Silver", "Palladium",
                                 "Platinum", "Rhodium"])

    parser.add_argument("-bg", "--buy_grams", default=None,
                        help="Specify the grams that you want to buy."
                        "(this argument must be used with bm)", type=int)

    parser.add_argument("-ea", "--employee_actions",
                        help="Actions that only and employee can do."
                             "Code allowed: rr to read the register;"
                             "gb to get the balance of""wallet and inventory;"
                             "pb to bay the bank loan", default=None, type=str,
                             choices=["rr", "gb", "pb"])

    args = parser.parse_args()
    return args


arg = parse_arguments()

username = arg.username
password = arg.password
metal = arg.buy_metal
grams = arg.buy_grams
adduser = arg.add_user
addemployee = arg.add_employee
e = arg.employee_actions

# First of all, we check if the user wants to register or log in
log = None
print('\n')

if addemployee is True:

    # The user wants to register as an employee, so we ask again the password

    cp = check_password(password)

    if cp is True:

        # The two passwords were equal, so we proceed to the registration
        # The validity of the email is different get checked by the function

        add_e = add_employee(username, password)

        if add_e is True:
            print("The registration was successful! \n")

elif adduser is True:

    # The user wants to register as a client, we first of all verify the email

    valid_mail = verify_user(username)

    if valid_mail is True:

        # The email in in the correct format and allowed to be registered
        # We check the password

        cp = check_password(password)

        if cp is True:

            # The two passwords are the same, we ask data on the credit card
            # The functions on credit card control the format of input

            number = get_number()
            date = get_date()
            cvc = get_cvc()
            add_user(username, password, number, date, cvc)
else:
    log = log_in(username, password)

if log is not None:
    if log == 'employee':

        if metal is not None or grams is not None:
            print('Sorry but as an employee you are not allowed'
                  'to buy metals from our company. \n')

        if e == "rr":
            read_register()

        elif e == "gb":
            get_balance()

        elif e == "pb":
            pay_loan()

        elif e is None:
            print('You succesfully logged in as a employee,'
                  'but you have to type other arguments to do something. \n')

    elif log == 'user':
        if metal is None:
            print('To buy metals you have to specify'
                  'them using --buy_metal. \n')

        elif grams is None:
            print('To buy metals you have to specify'
                  'the grams you want using --buy_grams. \n')

        else:
            check_cvc = ask_cvc(username)
            buy_metal(username, metal, grams, check_cvc)

        if e is not None:
            print('You tried to call a function that your user is'
                  'not allowed to launch. As a user you are only allowed'
                  'to buy metals from our company. \n')
