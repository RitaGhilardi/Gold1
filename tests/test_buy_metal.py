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
        self.f_mail = "rita"
        self.f_metal = "Wood"
        self.f_quantity = "0"
        
    def test_buy_metal(self):
        #self.assertTrue(buy_metal(self.mail, self.metal, self.quantity))
        #self.assertFalse(buy_metal(self.mail, self.f_metal, self.quantity))
        #self.assertFalse(buy_metal(self.mail, self.metal, self.f_quantity))
        self.assertFalse(buy_metal(self.f_mail, self.metal, self.quantity))


if __name__ == "__main__":
    unittest.main()