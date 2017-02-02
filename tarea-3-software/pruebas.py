'''
Created on 2 feb. 2017

@author: carlos
@author: pablo
'''
import unittest
from main import *


class Test(unittest.TestCase):


    def testCedulaNegativa(self):
        billetera = BilleteraElectronica(0,"Pablo","Betancourt",-1,1234)

if __name__ == "__main__":
    unittest.main()