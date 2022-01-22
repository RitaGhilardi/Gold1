def get_number():

    ''' This is one of the functions called during the registering of a new
        user. This function ask the user to insert the enumber of its credit
        card (maximum 3 times), check its validity and return it.
    '''

    # Set some parameters for the while cycle

    cc = False
    i = 0

    while cc is False:

        number = str(input(('Please insert your credit card number.'
                            'It should be composed by 16 number and no'
                            'letters or symbols. \n')))

        good = False

        # Check if the input was empty

        if number:

            # Check if the input contains only numerical characters

            int_number = '0123456789'
            valid = True
            for n in number:
                if n not in int_number:
                    print('Error, typed a letter or a special character. \n')
                    valid = False
                    break

            if valid is True:
                nnumber = int(number)

                # Check if the credit card number has the right format

                if (len(number) == 16 and nnumber > 0 and
                        nnumber <= 9999999999999999):
                    good = True
        else:
            print('Error, you did not enter any number. \n')

        if good is True:
            cc = True
            print('The number was accepted. \n')

        # Check if the user tried more than 3 times to enter the input

        elif i >= 2:
            print('Fatal error, the credit card number is not on the',
                  'correct format and you reached the limit of chances',
                  'that you had. Try again to register to our website. \n')
            break

        # Increase i if the input was wrong

        elif good is False:
            i = i + 1

    if cc is False:
        number = None

    return number
