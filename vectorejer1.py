# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 11:07:09 2020

@author: luisa
"""


from random import randint
from time import sleep
auxiliar = int()
vector = [int() for ind0 in range(100)]
print("Ingrese el tamano del vector: ")
tamanovector = int(input())
for i in range (1, tamanovector+1):
    vector[i - 1] = randint(0, 99)
    print("El valor en la posicion ", i , "es", vector[i-1])
    sleep(1)
sleep(1)
for j in range (1, tamanovector+1):
    for l in range (1, tamanovector):
        if vector[1-1]<vector[1]:
            auxiliar = vector[1-1]
            vector[1-1] = vector[1]
            vector[1] = auxiliar
for k in range(1, tamanovector+1):
    print("El vector ordenado en la posicion ", k , "es ", vector[k-1])
    sleep(1)