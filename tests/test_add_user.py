#! /usr/bin/env python3
import unittest
import sys
import os

# add parent folder to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from packages.add_user import add_user

class Test(unittest.TestCase):
    def setUp(self):
    
        # valid inputs
        self.user1 = "eva.castelli@gmail.com"
        self.user2 = "giacomo@hotmail.it"
        self.user3 = "pietro.belligoli@student.h-farm.com"
        self.pass1 = "Pallocchio"
        self.pass2 = "Ciaociao"
        self.pass3 = "Password!!"
        
        # invalid inputs
        self.f_mail1 = "roberto.celi@gmail.com"
        self.f_mail2 = "luca@gold1.com"
        self.f_mail3 = []
        
    def test_valid_inputs(self):
        self.assertTrue(verify_user(self.user1, self.pass1))
        self.assertTrue(verify_user(self.user2, self.pass2))
        self.assertTrue(verify_user(self.user3, self.pass3))
        
    def test_invalid_inputs(self):
        self.assertFalse(verify_user(self.f_mail1, self.pass1))
        self.assertFalse(verify_user(self.f_mail2, self.pass2))
        self.assertFalse(verify_user(self.f_mail3, self.pass3))
        
if __name__ == "__main__":
    unittest.main()
