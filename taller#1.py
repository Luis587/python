# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 14:17:40 2020

@author: luisa
"""

llantas = int(input("Cantidad de llantas: "+"\n\t\t"))
costo = int(input("Precio unitario:"+"\n\t\t"))
resp0 = llantas * costo
resp1 = costo * 0.1 # El 10%
resp2 = resp0 - resp1

if llantas >= 5 :
    print("Valor a pagar: ", resp2)
elif llantas >= 1 and llantas <= 4 :
    print("Valor a Pagar: ", resp0)
else:
    print("no selecciono un valor")
