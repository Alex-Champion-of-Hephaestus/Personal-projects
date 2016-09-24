# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def xy(t,yi,vy,xi,vx):
   x= xi+vx*t
   y=yi+vy*t+.5*(-9.8)*t**2
   print("it is ", x, " units in the x direction from the origin")
   
   print("it is ", y, " units in the y direction from the origin")