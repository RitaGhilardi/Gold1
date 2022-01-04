import pandas as pd

def ask_cvc(user):

    ''' This function get called after the check done by the log_in function,
        so we are sure that the user is correctly registered into our database.
        The function take the cvc of the user stored in the database, ask the user
        to insert it again (maximum 3 times) and verify it.
    '''
    
    user_df = pd.read_csv (r'csv_files/db_users.csv')
    cvc_df = pd.read_csv (r'csv_files/info_users.csv')    
    check = False
    
    #Search the ID using the username. This value will be find by construction, because we already did the log in
    
    for i in range(len(user_df.index)):
        if user_df.loc[i,'email'] == user:
            user_id = user_df.loc[i,'ID']
            break
            
    #Search the cvc using the ID. This value will be find by construction, because we already did the log in
    
    for i in range(len(cvc_df.index)):
        if cvc_df.loc[i,'ID'] == user_id:
            stored = cvc_df.loc[i,'cvc']
            break
            
    #Ask to confirm the cvc
    
    i=0

    while check == False:
        number = str(input('Please insert the CVC of your credit card number to confirm the purchase. \n'))
        
        good = False
        
        #Check if the input was empty
        
        if number :
            
            #Check if the input contains only numerical characters
            
            int_number = '0123456789'
            valid = True
            for n in number:
                if n not in int_number:
                    print('Error, you typed a letter or a special character. \n')
                    valid = False
                    break 
            if valid == True:
                nnumber = int(number)
                if len(number) == 3 and nnumber > 0 and nnumber <= 999:
                    if nnumber == stored:                    
                        good = True
                    else:
                        print('Sorry, the cvc is not correct. \n')
                else:
                    print('We are sorry but the cvc was not in the correct format. It should be a number composed of 3 digits. \n')
        
        else:
            print('Error, you did not enter any number. \n')
            
        if good == True:
            check = True
            print('The number was accepted. \n')

        #Check if the user tried more than 3 times to enter the input
        
        elif i >= 2:
            print('Fatal error, the credit card cvc is not on the correct format or is not correct, and you reached the limit of chances that you had. Please try again to register to our website. \n')
            break
            
        #Increase i if the input was wrong
        
        elif good == False:                    
            i = i + 1
    
    return check

