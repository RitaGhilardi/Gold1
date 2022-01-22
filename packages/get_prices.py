import requests


def get_prices():

    ''' This function get called by the function "buy_metals" when in the
        inventory there is not enough of some metals. The function calls and
        API to get all the current prices of metals and modify them go have
        price per grams. The function return a dictionary with the current
        prices and a boolean variable that state if the API was online and
        so if the dictionary is full of trustable values.
    '''

    # Create the correct link

    symbol = 'XAU,XAG,XPD,XPT,XRH'
    base_currency = 'EUR'
    endpoint = 'latest'
    access_key = 'o65ww2g1zd18fqm7euy9h2at766a9amft1r6srflwfle1gqu6lx029fshbfu'

    # Request to the API

    resp = requests.get('https://metals-api.com/api/' + endpoint
                        + '?access_key=' + access_key + '&base='
                        + base_currency + '&symbols=' + symbol)
    s = resp.json()['success']

    if s is False:
        proces = None

    else:

        rates = resp.json()['rates']

        # Convert values in Euro over grams and add more readable names

        oz = 28.3495

        conversion = {'XAU': 'Gold',
                      'XAG': 'Silver',
                      'XPD': 'Palladium',
                      'XPT': 'Platinum',
                      'XRH': 'Rhodium'}

        prices = {}

        for key in rates.keys():
            prices[conversion[key]] = round((rates[key]/oz), 3)

    return(s, prices)
