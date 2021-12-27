import pandas as pd
import argparse
import hashlib
from email_validator import validate_email, EmailNotValidError

def add_employee(email, password):
    
    df_employees = pd.read_csv(r"csv_file/employees.csv")
    db_employees = pd.read_csv(r"csv_file/db_employees.csv")
    
    try: 
        valid = validate_email(email)
        email = valid.email
        
        if "@gold1.com" not in email:
            print("Please enter an employee email")

        else:
            check = False
            for mail in db_employees["email"]:
                if mail == email:
                    check = True
                    print("This account is already registered")
                    break

            if check == False:     
                presence = False
                for mail in df_employees["Email"]:
                    if email == mail:
                        presence = True
                        digest_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
                        new_df = pd.DataFrame({"email": [email], "password": [digest_password]})
                        db_employees = db_employees.append(new_df)
                        db_employees.to_csv(r"csv_file/employees.csv", index = False)
                        print("Registration was successful!")
                        break

                if presence == False: 
                    print("No correspondence")
                    
    except EmailNotValidError as e:
        print(str(e))
