# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 14:37:57 2020

@author: luisa
"""


def fibonacci(n):
    a , b = 0,1
    while a <= n:
        print(a, end=' ')
        """c = a+b
        a = b
        b = c"""
        a, b = b, a+b
    print()
#fibonacci(8)