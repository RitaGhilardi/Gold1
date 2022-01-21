import unittest
import sys
import os

# add parent folder to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from packages.verify_user import verify_user


class Test(unittest.TestCase):

    def setUp(self):
        
        ''' The setup() function runs when the program starts.
            It is used to set the initial environment properties.
        '''

        # valid inputs
        self.user1 = "eva.castelli@gmail.com"
        self.user2 = "giacomo@hotmail.it"
        self.user3 = "pietro.belligoli@student.h-farm.com"

        # invalid inputs
        self.f_mail1 = "roberto.celi@gmail.com"
        self.f_mail2 = "luca@gold1.com"
        self.f_mail3 = []
        self.f_mail4 = ""
        self.f_mail5 = "ciao"
        self.f_mail6 = "anna@me"

    def test_valid_inputs(self):
    
        ''' This function tests the valid inputs of the verify_user() function.
        '''
        
        self.assertTrue(verify_user(self.user1))
        self.assertTrue(verify_user(self.user2))
        self.assertTrue(verify_user(self.user3))

    def test_invalid_inputs(self):
    
        ''' This function tests the invalid inputs of the verify_user() function.
        '''
        
        self.assertFalse(verify_user(self.f_mail1))
        self.assertFalse(verify_user(self.f_mail2))
        self.assertFalse(verify_user(self.f_mail3))
        self.assertFalse(verify_user(self.f_mail4))
        self.assertFalse(verify_user(self.f_mail5))
        self.assertFalse(verify_user(self.f_mail6))


if __name__ == "__main__":
    unittest.main()
