import pandas as pd
import argparse
import hashlib

def add_user(email, password):
    
    db_users = pd.read_csv(r"csv_files/db_users.csv")
    
    suffix = email.split("@")[1]
   
    
    if suffix == "gold1.com":
        print("Invalid email")
        
    else:
        digest_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        new_df = pd.DataFrame({ "ID": [len(db_users["password"])+1], "email": [email], "password": [digest_password]})
        new_df.to_csv('db_users.csv', mode = "a", index = False, header = False)
        print("Registration was successful")