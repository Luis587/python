# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 12:31:50 2020

@author: luisa
"""


hostnames = ["R1","R2","R3","S1","S2"]
print(type(hostnames))
print(len(hostnames))
print(hostnames)
print(hostnames[0])
print(hostnames[1])
print(hostnames[2])
print(hostnames[3])
print(hostnames[4])
print(hostnames[-1])
print(hostnames[-2])

hostnames[4]= "S4"
del hostnames[5]

