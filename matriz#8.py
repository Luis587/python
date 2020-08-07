# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 12:11:16 2020

@author: luisa
"""


a = [[0,0,0,0,0] , [0,0,0,0,0],
     [0,0,0,0,0] , [0,0,0,0,0] ,
     [0,0,0,0,0]]
for i in range (0,5):
    for j in range (0,5):
        print("Ingrese el valor para la posicion: ",i,j)
        a[i][j]=int(input())
print(a)