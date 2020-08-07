# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 13:54:59 2020

@author: luisa
"""


def isYearLeap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                resp = 'Es Bisisesto'
            else:
                resp = 'No es Bisiesto'
        else:
            resp = 'Es Bisiesto'
    else:
        resp = 'No es bisiesto'
    return resp
def daysInMonth(year, month):
    if isYearLeap(year) and month ==2:
        return 29
    elif month == 2 :
        return 28
    elif month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    else:
        return None
print(daysInMonth(1900,2))


