import pandas as pd
import argparse
import hashlib

def log_in(email, password):
    
    db_users = pd.read_csv(r'csv_file/db_users.csv')
    db_employees = pd.read_csv(r'csv_file/db_employees.csv')

    suffix = email.split("@")[1]
   
    #employees
    if suffix == "gold1.com":
        
        for address in db_employees["email"]:
            if address == email:
                line = list(db_employees["email"]).index(address)
                digest_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
                if db_employees["password"][line] == digest_password:
                    print("Access allowed")
                    break
                
                else:
                    print("Please check password")
                    break
                
                
            elif address != email and list(db_employees["email"]).index(address) == len(db_employees["email"])-1:
                print("Please, log-in as a user")
            
                
            else: 
                continue
        
      
    #users   
    else: 
      
        for mail in db_users["email"]:
            if mail == email:
                line = list(db_users["email"]).index(mail)
                digest_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
                if db_users["password"][line] == digest_password:
                    print("Access allowed")
                    break
                
                else:
                    print("Please check password")
                    break
                
                
            elif mail != email and list(db_users["email"]).index(mail) == len(db_users["email"])-1:
                print("No correspondence")
            
                
            else: 
                continue
