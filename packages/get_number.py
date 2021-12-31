def get_number():
    cc = False
    i=0

    while cc == False:
        
        number = str(input('Please insert your credit card number. It should be composed by 16 number and no letters or symbols. \n'))
        
        good = False
        
        if number:
            int_number = '0123456789'
            valid = True
            for n in number:
                if n not in int_number:
                    print('Error, you typed a letter or a special character. \n')
                    valid = False
                    break 
            if valid == True:
                nnumber = int(number)
                if len(number) == 16 and nnumber > 0 and nnumber <= 9999999999999999:
                    good = True
        else:
            print('Error, you did not enter any number. \n')
            
        if good == True:
            cc = True
            print('The number was accepted. \n')

        elif i >= 2:
            print('Fatal error, the credit card number is not on the correct format and you reached the limit of chances that you had. Please try again to register to our website. \n')
            break
            
        elif good == False:                    
            i = i + 1
            
    if cc == False:
        number = None
    
    return number