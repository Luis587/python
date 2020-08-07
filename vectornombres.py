# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 11:34:06 2020

@author: luisa
"""


nombtre = str()
auxiliar = str()
vector = [int() for ind0 in range(100)]
print("Ingrese el tamano del vector: ")
tamanovector = int(input())
for i in range (1, tamanovector+1):
    print("Ingrese el nombre del estudiante")
    nombre = input()
    vector [i-1]= nombre
    print("el valor en la posicion ",i, " es ",vector[i-1])
for j in range (1, tamanovector+1):
    for l in range (1, tamanovector):
        if vector[l-1]>vector[l]:
            auxiliar = vector[l-1]
            vector[l-1] = vector[l]
            vector[l] = auxiliar
for k in range(1, tamanovector+1):
    print("El vector ordenado en la posicion ", k , "es ", vector[k-1])