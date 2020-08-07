# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 11:36:51 2020

@author: luisa
"""


def direccion(calle,sector,codigopostal,referencia,numcasa):
    print("Sector del domicilio: ", sector, "Calle: ",calle)
    print("Numero de casa: ", numcasa)
    print("Referencia: ", referencia)
    print("Codigo postal: ", codigopostal)
    
print("Ingrese los datos solicitados")
s = input("ingrese sector de residencia: ")
c = input("Ingrese calle: ")
num = input("# de casa: ")
r = input("Referencia de su domicilio: ")
cod = input("Codigo Postal: ")

direccion(s,c,num,r,cod)