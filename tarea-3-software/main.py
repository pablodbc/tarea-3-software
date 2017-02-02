# -*- encoding: utf-8 -*-
'''
Created on 1 feb. 2017

@author: carlos
'''
from datetime import *

class Registro:
    def __init__(self, monto, fecha, localID):
        self.monto = monto
        self.fecha = datetime.strftime(fecha,'%d/%m/%Y %H:%M')
        self.localID = localID

    def __str__(self):
        return "\nMonto: "+str(self.monto)+"\nFecha: "+self.fecha+"\nEstablecimiento: "+str(self.localID)+"\n"

class BilleteraElectronica:
    def __init__(self, identificador, nombres, apellidos, CI, PIN, balance = 0):
        self.identificador = identificador
        self.nombres = nombres
        self.apellidos = apellidos
        assert(CI >=0)
        self.CI = CI
        self.PIN = PIN
        self.recargas = []
        self.consumos = []
        self.balance = balance

    def recargar(self, monto, localID,fecha = datetime.now()):
        assert(monto > 0)
        self.recargas += [Registro(monto, fecha, localID)]
        self.balance += monto
