# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 11:43:42 2020

@author: luisa
"""


def isYearLeap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                resp = 'True'
            else:
                resp = 'False'
        else:
            resp = 'True'
    else:
        resp = 'False'
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
def dayOfYear(year, month, day):
    if isYearLeap(year):
        D = 1
    else:
        D = 2
    C = int((275 * month) / 9.0) - D * int((month + 9) / 12.0) + day - 30
    return C

def days_year(year,C):
      
    if isYearLeap(year):
        D = 1
    else:
        D = 2
    month = int((9 * (D + C)) / 275.0 + 0.98)
    if C < 32:
        month = 1
    day = C - int((275 * month) / 9.0) + D * int((month + 9) / 12.0) + 30
    return year, month, day
print(dayOfYear(2000, 12, 31))
