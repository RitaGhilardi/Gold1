#! /usr/bin/env python3
import unittest
import sys
import os

# add parent folder to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from packages.buy_metals import buy_metal

class Test(unittest.TestCase):
    def setUp(self):
    
        self.mail = "giada.rovari@gmail.com"
        self.metal = "Silver"
        self.quantity = "1"
        self.check = True
        self.f_metal = "Wood"
        self.f_quantity = "0"
        self.f_check = False
        
        
    def test_buy_metal(self):
    
        #We inserted f_mail to be complete but we are not testing it because the function
        #buy metals do not check it. Buy_metals runs only after the log_in, so the user is 
        #already verified.
        
        #self.assertTrue(buy_metal(self.mail, self.metal, self.quantity, self.check))
        #self.assertFalse(buy_metal(self.mail, self.f_metal, self.quantity, self.check))
        #self.assertFalse(buy_metal(self.mail, self.metal, self.f_quantity, self.check))
        self.assertFalse(buy_metal(self.mail, self.metal, self.quantity, self.f_check))



if __name__ == "__main__":
    unittest.main()