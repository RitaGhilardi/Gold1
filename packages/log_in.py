import pandas as pd
import argparse
import hashlib
from email_validator import validate_email
from email_validator import EmailNotValidError

def log_in(email, password):
    
    db_employees = pd.read_csv(r'csv_file/db_employees.csv') 
    db_users = pd.read_csv(r'csv_file/db_users.csv')
    r = None

    try:
        valid = validate_email(email)
        email = valid.email
        suffix = email.split("@")[1]
        if suffix == "gold1.com": 

        # Employee
            for address in db_employees["email"]: 
                if address == email:
                    line = list(db_employees["email"]).index(address)
                    digest_password = hashlib.sha256(password.encode
                                                     ('utf-8')).hexdigest()

                    if db_employees["password"][line] == digest_password:
                        print("Access allowed. \n")
                        r = 'employee'
                        break 
                    else:
                        print("Please check password. \n")
                        break 
                elif (address != email and list(db_employees["email"])
                      .index(address) == len(db_employees["email"])-1):
                    print('Does not  exist')  
                else:
                    continue

        # Users
        else:
            for mail in db_users["email"]:
                if mail == email:
                    line = list(db_users["email"]).index(mail)
                    digest_password = hashlib.sha256(password.encode
                                                     ('utf-8')).hexdigest()

                    if db_users["password"][line] == digest_password:
                        print("Access allowed. \n")
                        r = 'user'
                        break 
                    else:
                        print("Please check password. \n")
                        break
                elif (mail != email and list(db_users["email"])
                      .index(mail) == len(db_users["email"])-1):
                    print('Does not  exist')

    except EmailNotValidError as e:
        print(str(e))
    return r
