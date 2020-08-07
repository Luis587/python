# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 12:38:03 2020

@author: luisa
"""


length=int(input("Ingrese cantidad de temperaturas [1,10]: "))
matrix1=[]
matrix2=[]
gas = 0
liq = 0
sol = 0
opc = 0
sum1 = 0
sum2 = 0
while length<1 or length>10:
    print("El valor debe ser entre 1 y 10")
    length=int(input("Ingrese cantidad de temperaturas [1,10]: "))
if length>=1 and length<=10:
    for i in range(1,length+1):
        print("Temperatura ",i," en °C:")
        x=int(input())
        matrix1.append(x)
        opc+=1
    for j in range(0,length):
        if matrix1[j]>=100:
            gas+=1
        if matrix1[j]>1 and matrix1[j]<100:
            liq+=1
        if matrix1[j]<=0:
            sol+=1
    print("\t\t\t","RESUMEN DEL ANÁLISIS DE MUESTRAS DE AGUA","\n\n")
    print("Cantidad de muestras sólidas: ",sol,"\n")
    print("Cantidad de muestras líquidas: ",liq, "\n")
    print("Cantidad de muestras gaseosas: ",gas, "\n")
    for r in range(0,length):
        sum1 += matrix1[r]
    promedio1 =sum1/opc
    print('Temperatura Promedio °C: ',promedio1, "\n")
    for t in range(0,length):
        faren=(matrix1[t] * 1.8)+32
        matrix2.append(faren)
    for u in range(0,length):
        sum2+=matrix2[u]
    promedio2=sum2/opc
    print('Temperatura Promedio °F: ',promedio2, "\n")