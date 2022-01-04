import pandas as pd

def pay_loan():
    
    ''' This function can be called only by employees. The 
        function check if there are money due to banks, check
        the availability of money of the company and repay 
        part or all the bank loan using all the available money.
    '''
    
    w = pd.read_csv(r'csv_files/wallet.csv')

    #Control if there are bank loan to be repaid

    if w.loc[0, 'Bank_Loan'] == 0:

        print('There are no debts to be repaid')

    elif w.loc[0, 'Balance'] == 0:

        print('You have no money to repay your bank loan') 

    else:

        if w.loc[0, 'Bank_Loan'] <= w.loc[0, 'Balance']:

            #Pay all the bank loan
            amount = w.loc[0, 'Bank_Loan']
            w.loc[0, 'Balance'] = w.loc[0, 'Balance'] - amount
            w.loc[0, 'Bank_Loan'] = 0
            print('You have just paid', amount,
                  'EUR to the bank and now you have no more debts')

        else:

            #Gives all the money we have to repay part of the bank loan

            amount = w.loc[0, 'Balance']
            w.loc[0, 'Bank_Loan'] = w.loc[0, 'Bank_Loan'] - amount 
            w.loc[0, 'Balance'] = 0

            print('You have just paid', amount, 'EUR to the bank,',
                  'but you still have a debt of',
                  w.loc[0, 'Bank_Loan'], 'EUR')

        w.to_csv(r'csv_files/wallet.csv', index=False)