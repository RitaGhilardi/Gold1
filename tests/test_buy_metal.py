import unittest
import sys
import os
import pandas as pd

# add parent folder to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from packages.buy_metals import buy_metal


class Test(unittest.TestCase):

    def setUp(self):

        ''' The setup() function runs when the program starts.
            It is used to set the initial environment properties.
        '''

        # Valid inputs
        self.mail1 = "giada.rovari@gmail.com"
        self.mail2 = "robertoceli@gmail.com"
        self.metal1 = "Silver"
        self.metal2 = "silver"
        self.quantity1 = 1
        self.quantity2 = 1000
        self.check = True

        # Invalid inputs
        self.f_metal1 = "Wood"
        self.f_metal2 = ""
        self.f_quantity1 = -2
        self.f_quantity2 = 0
        self.f_quantity3 = "12"
        self.f_check = False

    def test_valid_inputs(self):

        ''' This function tests the valid inputs
            of the buy_metal() function.
        '''

        self.assertTrue(buy_metal(self.mail1, self.metal1, self.quantity1,
                                  self.check))
        self.assertTrue(buy_metal(self.mail2, self.metal2, self.quantity2,
                                  self.check))
        register = pd.read_csv(r'csv_files/register.csv')
        fixture = register[:-2]
        fixture.to_csv(r'csv_files/register.csv', index=False)

    # We are not testing invalid emails because the function
    # buy_metal() doesn't check them. In fact, buy_metal() runs only after the
    # log_in(), so the user has been already verified.

    def test_invalid_inputs(self):

        ''' This function tests the invalid inputs of the buy_metal() function.
        '''

        self.assertFalse(buy_metal(self.mail1, self.f_metal1, self.quantity1,
                                   self.check))
        self.assertFalse(buy_metal(self.mail1, self.metal1, self.f_quantity1,
                                   self.check))
        self.assertFalse(buy_metal(self.mail1, self.f_metal2, self.quantity1,
                                   self.check))
        self.assertFalse(buy_metal(self.mail1, self.metal1, self.f_quantity2,
                                   self.check))
        self.assertFalse(buy_metal(self.mail1, self.metal1, self.f_quantity3,
                                   self.check))
        self.assertFalse(buy_metal(self.mail1, self.metal1, self.quantity1,
                                   self.f_check))


if __name__ == "__main__":
    unittest.main()
