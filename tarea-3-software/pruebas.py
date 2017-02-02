'''
Created on 2 feb. 2017

@author: carlos
@author: pablo
'''
import unittest
from main import *


class Test(unittest.TestCase):

	# Casos maliciosos
    def testCedulaNegativa(self):
        billetera = BilleteraElectronica(0,"Pablo","Betancourt",-1,1234)

    def testRecargaNoValida(self):
            billetera = BilleteraElectronica(0,"Pablo","Betancourt",1,1234)
            billetera.recargar(-1000,"Pablo")
    
    def testDebitoConBalanceMenor(self):
        billetera = BilleteraElectronica(0,"Pablo","Betancourt",1,1234)
        billetera.consumir(1234,1,"Pablo")

    # Casos Frontera
    def testDebitoConBalanceMinimamenteMayor(self):
            billetera = BilleteraElectronica(0,"Pablo","Betancourt",1,1234,1.000001)
            billetera.consumir(1234,1,"Pablo")

    # Caso esquina: Consumo con balance minimamente menor explotando
    # explotando fallas de precision
    def testDebitoConBalanceMinimamenteMenor(self):
        billetera = BilleteraElectronica(0,"Pablo","Betancourt",1,1234,0.9999999999999999999999999)
        billetera.consumir(1234,1,"Pablo")

    def testNombreConLetrasFueraDeLoNormal(self):
    	identificador, nombres, apellidos, CI, PIN = 0,"ñññññ","áááááááááá",1,1234
    	billetera = BilleteraElectronica(identificador, nombres, apellidos, CI, PIN)
    	assert(billetera.identificador == identificador)
    	assert(billetera.nombres == nombres)
    	assert(billetera.apellidos == apellidos)
    	assert(billetera.CI == CI)
    	assert(billetera.PIN == PIN)
    	assert(billetera.balance == 0)

    def testBalanceConsistente(self):
    	identificador, nombres, apellidos, CI, PIN,balance = 0,"ñññññ","áááááááááá",1,1234,3
    	billetera = BilleteraElectronica(identificador, nombres, apellidos, CI, PIN)
    	assert(billetera.balance  == 3)


if __name__ == "__main__":
    unittest.main()