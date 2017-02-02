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

    def testRecargaNoValida(self):
            billetera = BilleteraElectronica(0,"Pablo","Betancourt",1,1234)
            billetera.recargar(-1000,"Pablo")
    
    def testDebitoConBalanceMenor(self):
        billetera = BilleteraElectronica(0,"Pablo","Betancourt",1,1234)
        billetera.consumir(1234,1,"Pablo")

    def testDebitoConBalanceMinimamenteMayor(self):
            billetera = BilleteraElectronica(0,"Pablo","Betancourt",1,1234,1.000001)
            billetera.consumir(1234,1,"Pablo")

if __name__ == "__main__":
    unittest.main()