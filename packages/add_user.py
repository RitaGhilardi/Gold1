import pandas as pd
import argparse
import hashlib
import random
from email_validator import validate_email
from email_validator import EmailNotValidError


def add_user(email, password, number, date, cvc):

    ''' This function add a user to the csv "db_users.csv",
        that is necessary for an employee to log in, and to register
        the informations of the new user's credit card on the dataset
        "info_users.csv".   
    '''
               
    if number is None or date is None or cvc is None:
        print('Something in the registration process'
              ' went wrong. Please try again. \n')
    else:
        print('You successfully registered. Now'
              ' you are allowed to buy metals. \n')
        db_users = pd.read_csv(r'csv_files/db_users.csv')
        
        # Generate the random ID without call too many times
        # Generate a random in an interval with no valid ID
        # ID with min 1 and max 99999999
        existing_id = list(db_users['ID'])
        existing_id = sorted(existing_id)
        list_id = [0]
        list_id.extend(existing_id)
        list_id.extend([100000000])

        # Loop to check, but whould not be necessary
        new = False
        while new is False:
            delta = []
            best_i = 0
            for i in range(len(list_id)-1):
                delta.append(list_id[i+1]-list_id[i])
                if delta[i] > delta[best_i]:
                    best_i = i
            bottom = list_id[best_i]
            top = list_id[best_i+1]
            Id = random.randint(bottom+1, top-1)
            if Id not in list_id:
                new = True

        digest_password = hashlib.sha256(password.encode
                                         ('utf-8')).hexdigest()
        new = pd.DataFrame({"ID": [Id], "email": [email],
                            "password": [digest_password]})
        db_users = db_users.append(new)
        db_users.to_csv(r'csv_files/db_users.csv', index=False)
        info = pd.read_csv(r'csv_files/info_users.csv')
        new = pd.DataFrame({"ID": [Id], "number": [number],
                            "date": [date], "cvc": [cvc]})
        info = info.append(new)
        info.to_csv(r'csv_files/info_users.csv', index=False)
