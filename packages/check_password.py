def check_password(pw):

    c = False
    i = 0
    while c is False:

        check = str(input('Enter again the password'))

        

        if pw == check:
            c = True
            print('password was accepted)

        

        elif i >= 2:
            print('the two password still not coincide. Please try again to register to our website)
            break

        
        elif pw != check:
            i = i + 1
            print('The two password are not the same, enter again the password')

    return c