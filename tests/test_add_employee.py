import unittest
import sys
import os
import pandas as pd

# add parent folder to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from packages.add_employee import add_employee


class Test(unittest.TestCase):

    def setUp(self):
        
        ''' The setup() function runs when the program starts.
            It is used to set the initial environment properties.
        '''

        # valid inputs
        self.mail_empl = "marco.visentin@gold1.com"
        self.pass_empl = "Marco2000"

        # invalid inputs
        self.f_mail1 = "rita"
        self.f_mail2 = "ghilardi.rita@gold1.com"
        self.f_password1 = 3
        self.f_password2 = "."

    def test_valid_input(self):
    
        ''' This function tests the valid inputs of the add_employee() function.
        '''

        self.assertTrue(add_employee(self.mail_empl, self.pass_empl))
        db_employees = pd.read_csv(r'csv_files/db_employees.csv')
        fixture = db_employees[:-1]
        fixture.to_csv(r'csv_files/db_employees.csv', index=False)

    def test_invalid_inputs(self):
    
        ''' This function tests the invalid inputs of the add_employee function.
        '''
        
        self.assertFalse(add_employee(self.f_mail1, self.pass_empl))
        self.assertFalse(add_employee(self.mail_empl, self.f_password1))
        self.assertFalse(add_employee(self.f_mail2, self.pass_empl))
        self.assertFalse(add_employee(self.mail_empl, self.f_password2))


if __name__ == "__main__":
    unittest.main()
