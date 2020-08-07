# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:16:45 2020

@author: luisa
"""

x =int(input("ingrese un numero a contar: "))
y = 1
z = 0
while y <= x:
     print(y, end=" ") #el end= me ayuda a que las repeticiones vayn en sentido horizontal
   # print(y)
     z += y
     y = y+1
     p = z / x
print("La suma de los # es: ", z)
print("el promedio total es: ", p)