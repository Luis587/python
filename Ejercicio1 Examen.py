# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 10:59:34 2020

@author: luisa
"""



inicial = int(input("Contador Inicial: "))
final = int(input("Contador Final: "))
print("\n")
print("1.Si desea imprimir blanco/negro")
print("\n")
print("2.Si desea imprimir a Color")
opc = int(input("Ingrese la opcion a ejecutar: "))

if opc == 1:       
        resp = final - inicial
        print("Impresiones: ", resp)
        costo = resp * 0.06
        print("Costo: $",costo)
elif opc == 2 :
    while final < inicial :
        print("Error: el contador inicial es menor que el final")
        final = int(input("Contador Final: "))
        resp2 = final - inicial
        print("Impresiones: ", resp2)
        costo2 = resp2 *.12
        print("Costo: $", costo2)
else:
    print("La opcion ingresada no es valida")
