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
        billetera = BilleteraElectronica(identificador, nombres, apellidos, CI, PIN,balance)
        assert(billetera.balance  == 3)

    def testConsistenciaClaseRegistro(self):
        monto, fecha, localID = 20, datetime.now(), 42 
        new = Registro(monto, fecha, localID)
        assert(new.monto == monto)
        assert(new.fecha == datetime.strftime(fecha,'%d/%m/%Y %H:%M'))
        assert(new.localID == localID)

    def testConsistenciaBalanceSaldo(self):
        identificador, nombres, apellidos, CI, PIN,balance = 0,"ñññññ","áááááááááá",1,1234,3
        new = BilleteraElectronica(identificador, nombres, apellidos, CI, PIN,balance)
        assert(new.saldo() == new.balance)

    def testConsistenciaRegistroRecargas(self):
        identificador, nombres, apellidos, CI, PIN,balance = 0,"ñññññ","áááááááááá",1,1234,3
        new = BilleteraElectronica(identificador, nombres, apellidos, CI, PIN,balance)
        for x in range(1, 11):
            new.recargar(10, 42)
            assert(len(new.recargas) == x)

    def testConsistenciaRegistroConsumos(self):
        identificador, nombres, apellidos, CI, PIN,balance = 0,"ñññññ","áááááááááá",1,1234,3
        new = BilleteraElectronica(identificador, nombres, apellidos, CI, PIN,balance)
        for x in range(1, 11):
            new.recargar(10, 42)
            new.consumir(1234,10, 42)
            assert(len(new.consumos) == x)

    def testConsistenciaConsumoBalance(self):
        identificador, nombres, apellidos, CI, PIN,balance = 0,"ñññññ","áááááááááá",1,1234,3
        new = BilleteraElectronica(identificador, nombres, apellidos, CI, PIN,balance)
        monto1,monto2 = 12,10
        new.recargar(monto1, 42)
        new.consumir(1234,monto2, 42)
        assert(new.balance == monto1 - monto2)



if __name__ == "__main__":
    unittest.main()