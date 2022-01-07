import pandas as pd
import argparse
import hashlib
from email_validator import validate_email
from email_validator import EmailNotValidError



def log_in(email, password):

    ''' This function takes the email and password given by the 
        user or employee and verify that they correspond to the 
        one stored into our database. The function return a values
        that is "None" if the password was wrong or the email not 
        registered, "employee" if the email was the correct one of 
        an employee of "user" if the email was the correct one of 
        a user.
    '''

    r = None
    
    if type(email) is not str or type(password) is not str:
        
        #Something wrong happened
        
        print('ERROR: one of the input is in an unexpected type.',
            'Please contact the customer service to notify the error. \n')
    
    else:
        
        #The input are of the correct type
    
        db_employees = pd.read_csv(r'csv_files/db_employees.csv')
        db_users = pd.read_csv(r'csv_files/db_users.csv')




        #Check if the email is valid
        
        try: 
            valid = validate_email(email)
            email = valid.email
            suffix = email.split("@")[1] 
            #Check if the people that want to log in is a employee
            if suffix == "gold1.com":




                # Employee
                for address in db_employees["email"]:
                    #Check the presence of the email
                    if address == email: 
                        line = list(db_employees["email"]).index(address)
                        digest_password = hashlib.sha256(password.encode 
                                                         ('utf-8')).hexdigest()
                        #Check if the password is correct
                        if db_employees["password"][line] == digest_password:
                            print("Access allowed. \n")
                            r = 'employee'
                            break
                        else:
                            print("Please check password. \n")
                            break
                     #Message if the suffix is gold1.com
                    #But the employee is not registered
                    elif (address != email and list(db_employees["email"])
                          .index(address) == len(db_employees["email"])-1):
                        print('We are sorry, but your employee account' 
                              ' does not exist. Register to our website'
                              ' before logging in.')
                    else:
                        continue




            # Users
            else:
                for mail in db_users["email"]:
                    #Check if the email match 
                    if mail == email:
                        line = list(db_users["email"]).index(mail)
                        digest_password = hashlib.sha256(password.encode 
                                                         ('utf-8')).hexdigest()
                        #Check if the password match
                        if db_users["password"][line] == digest_password:
                            print("Access allowed. \n")
                            r = 'user'
                            break
                        else:
                            print("Please check password. \n") 
                            break
                    #Print a different message if the email is not in our register
                    elif (mail != email and list(db_users["email"])
                          .index(mail) == len(db_users["email"])-1):
                        print('We are sorry but your account does not exist. ' 
                              'Please register yourself before log in')




        except EmailNotValidError as e:
            print(str(e)) 
    return r 
