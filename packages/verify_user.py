import pandas as pd
import argparse
import hashlib
import random
from email_validator import validate_email
from email_validator import EmailNotValidError

def verify_user(email):

    ''' This function controls that the email of the new user is in 
        the right format, is not already registered and is not a mail
        of an employee.    
    '''
    
    db_users = pd.read_csv(r'csv_file/db_users.csv')
    result = False

    if "@" not in email:
        print("Please enter a valid email. \n")

    else:
        suffix = email.split("@")[1]

        if suffix == "gold1.com":
            print("Invalid email, please register as a user. \n")

        else:
            try:
                valid = validate_email(email)
                email = valid.email

                # Check if the email is already registered

                presence = False

                for i in range(len(db_users)):
                    if email == db_users.loc[i, 'email']:
                        presence = True
                        print('The email is already associated'
                              ' to an account. \n')

                if presence is False:
                    result = True
                    print('Your email was accepted. \n')
                        
            except EmailNotValidError as e:
                print(str(e))

    return result