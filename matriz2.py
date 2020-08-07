# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 12:05:46 2020

@author: luisa
"""


import numpy as np

array = np.array([[1,2,3,4], [5,6,7,8]], dtype=np.int64)
print(array)
print("\n"*2)
unos = np.ones((4,4))
print(unos)
print("\n"*2)
ceros = np.zeros((4,4))
print(ceros)
print("\n"*2)
ran=np.random.random((4,4))
print(ran)
print("\n"*2)
ept = np.empty((5,5))
print(ept)
full=np.full((5,5),10)
print(full)
print("\n"*2) 
espacio1=np.arange(0,100+1,3)
print(espacio1)
print("\n"*2)
espacio2 = np.linspace(1,100,10)
print(espacio2)
print("\n"*2)
a = np.array([(1,2,3) , (4,5,6)], dtype=np.int64) 
print(a)
print("\n")
print("la matriz tiene: ",a.ndim, " dimensiones")
print("\n")
print("El tipo de datos de la matriz es: ", a.dtype)
print("\n")
print("El tamano de la matriz es: ",a.size)
print("\n")
print("La forma de la matriz es: ", a.shape)

