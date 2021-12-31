import pandas as pd 

def get_balance():

    ''' This function can be called only by employees and it does
        not return anything. This function prints all the amount 
        of metals in the inventory, the cash available to buy
        new metals and the amount of money due to bank.
    ''' 
    
    df_inventory = pd.read_csv(r'csv_file/inventory.csv') 
    df_wallet = pd.read_csv(r'csv_file/wallet.csv') 

    #Inventory balance 
    print('Inventory: \n') 
    for i in range(0, len(df_inventory)): 
        print(df_inventory.loc[i, 'Metal'], 'balance:', 
              df_inventory.loc[i, 'Quantity'], 'grams. \n') 

    #Cash available
    print('Cash available:', df_wallet.loc[0, 'Balance'], 'EUR', '\n') 

    #Bank loan
    print('Debt with bank:', df_wallet.loc[0, 'Bank_Loan'], 'EUR', '\n') 