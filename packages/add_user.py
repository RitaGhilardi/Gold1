import pandas as pd
import argparse
import hashlib
import random
from email_validator import validate_email, EmailNotValidError

def add_user(email, password):
    
    db_users = pd.read_csv(r"csv_files/db_users.csv")
    
    if "@" not in email:
        print("Please enter a valid email")
        
    else: 
        suffix = email.split("@")[1]
   
        if suffix == "gold1.com":
            print("Invalid email, please register as a user")
        
        else:
            try:
                valid = validate_email(email)
                email = valid.email
                
        # Generate the random ID without call too many times
        # Generate a random in an interval with no valid ID
        # ID with min 1 and max 99999999

        existing_id = list(db_users['ID'])
        existing_id = sorted(existing_id)

        list_id = [0]
        list_id.extend(existing_id)
        list_id.extend([100000000])

        # Loop to check, but should not be necessary

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
            new_id = random.randint(bottom+1, top-1)
            if new_id not in list_id:
                new = True
                
                digest_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
                new_df = pd.DataFrame({ "ID": new_id, "email": [email], "password":[digest_password]})
                new_df.to_csv('db_users.csv', mode = "a", index = False, header = False)
                print("Registration was successful!")


            except EmailNotValidError as e:
                print(str(e))
       