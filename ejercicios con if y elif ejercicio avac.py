# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 11:20:31 2020

@author: luisa
"""

espacio = ''
nombre = input('Ingrese su nombre: ')
apellido = input("Ingrese su apellido: ")
location = input("Ingrese su Ubicacion(Pais): ")
age = int (input("ingrese un rango de edad de 0 hasta los 60 anos"+"\n\n\t\t\t\t\t"))

print('\n','Datos personales','\n', 'Nombre ',nombre,'\n', 'Apellido: ',apellido,'\n', 'Ubicacion: ',location,'\n', 'edad: ',age)
if age >= 0 and age <= 9:
    print("nino")
elif age >= 10 and age <=15:
    print("preadolescente.")
elif age >= 16 and age <= 21:
    print("adolescente")
elif age >= 22 and age <= 40:
    print("adulto")
elif age >= 41 and age <= 60:
    print("adulto mayor")
else:
    print("la edad que ingreso no esta considerada")
