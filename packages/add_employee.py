import pandas as pd
import argparse
import hashlib
from email_validator import validate_email
from email_validator import EmailNotValidError


def add_employee(email, password):

    ''' This function add an employee to the csv "db_employees.csv"
        that is necessary for an employee to log in.
        This function control that the email of the employee
        is allowed and that the employee is not already registered.    
    '''

    df_employees = pd.read_csv(r'csv_files/employees.csv')
    db_employees = pd.read_csv(r'csv_files/db_employees.csv')

    # Check if the mail is valid format

    result = False

    try:
        valid = validate_email(email)
        email = valid.email

        # Check if the domain is the correct one

        if "@gold1.com" not in email:
            print("Please enter an employee email. \n")

        else:
            check = False

            # Check if the employee is already registered

            for mail in db_employees["email"]:
                if mail == email:
                    check = True
                    print("This account is already registered. \n")
                    break

            # Check if the email is allowed to register as an employee

            if check is False:
                presence = False
                for mail in df_employees["email"]:
                    if email == mail:
                        presence = True
                        print('You are allowed to '
                              'register as an employee. \n')

                        # Register the employee

                        digest_pass = hashlib.sha256(password.encode
                                                     ('utf-8')).hexdigest()
                        new_df = pd.DataFrame({"email": [email],
                                              "password": [digest_pass]})
                        db_employees = db_employees.append(new_df)
                        db_employees.to_csv(r'csv_files/db_employees.csv',
                                            index=False)
                        result = True
                        print("Registration was successful!. \n")

                        break

                if presence is False:
                    print("We are sorry, this email is not allowed"
                          "to register as an employee. \n")

    except EmailNotValidError as e:

        print(str(e))

    return result
