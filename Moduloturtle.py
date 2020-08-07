# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 11:10:59 2020

@author: luisa
"""


from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()