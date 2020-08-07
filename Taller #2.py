# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 15:14:15 2020

@author: luisa
"""


horast = int(input("Horas Trabajadas: "+"\n\t\t"))
tarifa = int(input("Tarifa por hora: "+"\n\t\t"))
descu = int(input("Descuentos: "+"\n\t\t"))
resp0 = horast - descu
resp1 = (resp0 * tarifa)/2
resp2 = (horast * tarifa) + resp1
resp3 = resp2 - descu
resp4 = horast * tarifa
if horast >= 41:
    print("Valor a Pagar: ", resp3)
elif horast <= 40:
    print("Valor a Pagar: ", resp4)
