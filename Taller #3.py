# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 15:45:39 2020

@author: luisa
"""


nota1 = int(input("Ingrese su primera calificacion: "+"\n\n\t\t"))
nota2 = int(input("Ingrese su segunda calificacion: "+"\n\n\t\t"))
nota3 = int(input("Ingrece su tercera calificacion: "+"\n\n\t\t"))

if nota1 < nota2 and nota3:
    resp1 = nota2 + nota3
    print("\n"+"Su calificacion total es: "+"\n\n\t",resp1)
elif nota2 < nota1 and nota3:
    resp2 = nota1 + nota3
    print("\n"+"Su calificacion total es: "+"\n\n\t", resp2)
elif nota3 < nota1 and nota2:
    resp3 = nota1 + nota2
    print("\n"+"Su calificacion total es: "+"\n\n\t", resp3)
else:
    print("El valor ingresado no es correcto")