#! /usr/bin/env python3
import argparse

from packages.log_in import log_in
from packages.add_employee import add_employee
from packages.add_user import add_user
from packages.buy_metals import buy_metal
from packages.pay_loan import pay_loan
from packages.read_register import read_register
from packages.get_balance import get_balance


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