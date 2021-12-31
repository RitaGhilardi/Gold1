def get_date():
    
    #Set some parameters for the while cycle
    
    cc = False
    i=0

    while cc == False:
        m = str(input('Please insert your credit card month on which it will expire (mm). \n'))
        y = str(input('Please insert your credit card year on which it will expire (yyyy). \n'))
        
        good = False
        
        #Check if the input were empty 
        
        if m and y:
            
            #Check if the input contains only numerical characters
            
            int_number = '0123456789'
            valid = True
            
            for n in m:
                if n not in int_number:
                    valid == False
                    break 
                
            for n in y:
                if n not in int_number:            
                    valid = False
                    break 
                
            if valid == True:
                
                #Check if the numbers typed have the correct format
                
                nm = int(m)
                ny = int(y)
                
                today = date.today()

                # dd/mm/YY
                d1 = today.strftime("%d/%m/%Y")
                ay=d1[6:]
                
                if len(m) <= 2 and len(y) == 4 and nm > 0 and nm < 13 and ny >= ay and ny < (ay + 6):
                    
                    #Check if the card is valid but expires this year
                    
                    if ny == ay:
                        from datetime import date
                        am = d1[3:5]
                        if m > am:
                            good = True
                        else:
                            print('Error, this credit card is no more valid. \n')
                            
                        
                    else:
                        good = True
                
                else:
                    print('Error, the data that you typed are not of the right format or is no more valid. Please enter a valid date om the format mm and then yyyy. \n')
            else:
                print('Error, you typed a letter or a special character. \n')
                            
        else:
            print('Error, you let one entry empty. \n')
        
        if good == True:
            cc = True
            print('The data was accepted. \n')
            
        #Check if the user tried more than 3 times to enter the input
        
        elif i >= 2:
            print('Fatal error, the credit card number is not on the correct format and you reached the limit of chances that you had. Please try again to register to our website. \n')
            break
            
        #Increase i if the input was wrong
        
        elif good == False:                    
            i = i + 1
            
        
    
    #Create the output based on the inputs and all the checks
    
    if cc == False:
        date = None
    else:
        date = m+'/'+y
    
    return date