#! /usr/bin/env python3
import unittest
import sys
import os

# add parent folder to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from packages.log_in import log_in

class Test(unittest.TestCase):
    
    def setUp(self):

        # valid inputs
        self.email_user = "roberto.celi@gmail.com"
        self.password_user = "Peru2021"
        self.email_empl = "rita.ghilardi@gold1.com"
        self.password_empl = "HeidieMilady2"
        
        # invalid inputs
        self.f_email_user = "roberto"
        self.f_password_user = "Italy"
        self.f_email_empl = ""
        self.f_password_empl = "Heidi1"


    def test_valid_inputs(self):
        self.assertTrue(log_in(self.email_user, self.password_user))
        self.assertTrue(log_in(self.email_empl, self.password_empl))
        
    def test_invalid_inputs(self):
        self.assertFalse(log_in(self.email_user, self.f_password_user))
        self.assertFalse(log_in(self.f_email_user, self.password_user))
        self.assertFalse(log_in(self.email_empl, self.f_password_empl))
        self.assertFalse(log_in(self.f_email_empl, self.password_empl))

    
if __name__ == "__main__":
    unittest.main()