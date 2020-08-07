# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 11:20:31 2020

@author: luisa
"""


aclNum = int (input("ingrese un rango de edad de 0 hasta los 60 anos"+"\n"))
print("\n")
if aclNum >= 0 and aclNum <= 9:
    print("Es nino")
elif aclNum >= 10 and aclNum <=15:
    print("Es preadolescente.")
elif aclNum >= 16 and aclNum <= 21:
    print("Es adolescente")
elif aclNum >= 22 and aclNum <= 40:
    print("adulto")
elif aclNum >= 41 and aclNum <= 60:
    print("adulto mayor")
else:
    print("la edad que ingreso no esta considerada")
