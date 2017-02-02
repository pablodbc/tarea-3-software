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
