def get_cvc():
    cc = False
    i = 0

    while cc is False:
        number = str(input('Please insert the CVC of your credit card number.'
                           'It should be composed by 3 number'
                           'and no letters or symbols. \n'))

        good = False

        if number:
            int_number = '0123456789'
            valid = True
            for n in number:
                if n not in int_number:
                    print('Error, you typed a letter'
                          'or a special character. \n')
                    valid = False
                    break
            if valid is True:
                nnumber = int(number)
                if len(number) == 3 and nnumber > 0 and nnumber <= 999:
                    good = True

        else:
            print('Error, you did not enter any number. \n')

        if good is True:
            cc = True
            print('The number was accepted. \n')

        elif i >= 2:
            print('Fatal error, '
                  'the credit card number is not on the correct format'
                  'and you reached the limit of chances that you had.'
                  'Please try again to register to our website. \n')
            break

        elif good is False:
            i = i + 1

    if cc is False:
        number = None

    return number
