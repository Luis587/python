# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 11:09:42 2020

@author: luisa
"""
import numpy as np

num_filas= int(input("Inserte el numero de filas para la matriz: "))
num_columnas = int(input("Inserte el numero de columnas para la matriz: "))
matriz = np.zeros((num_filas, num_columnas))
print(matriz)
for i in range(0, num_filas):
    for j in range(0, num_columnas):
        print("Ingrese los valores para la posicion: ",i,j)
        matriz[i][j]=int(input())
print("\n")
print(matriz)
print("\n")
print("El valor de la diagonal principal de la matriz es: ")
matriz_diag = np.diag(np.diag(matriz))
print("\n")
print (matriz_diag)
print("\n")
print("El valor de la diagonl secuandaria es: ")
matriz_diag2 = np.fliplr(matriz).diagonal()
print("\n")
print(matriz_diag2)
