# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 13:21:13 2020

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

year = int(input("Introduzca un ano: "))
print(year, isYearLeap(year))

testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")


