# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 19:50:26 2016

@author: alexander
"""

def law_sines(A,B,C,a,b,c):
    import numpy as np
    from np import(sin,arcsin, radians)
    if solve is "side" is True:
        if A is None:
            if a and B and b is not None:
                A=sin((radians(a))*B)/sin(radians(b))
                print("A is ",A,"B is ",B,"C is ",C,"a is ",a,"b is ",b,"c is ",c,)
            if a and C and c is not None:
                A=sin((radians(a))*C)/sin(radians(c))
                print("A is ",A,"B is ",B,"C is ",C,"a is ",a,"b is ",b,"c is ",c,)
        if B is None:
            if b and A and a is not None:
               B=sin((radians(b))*A)/sin(radians(a))
               print("A is ",A,"B is ",B,"C is ",C,"a is ",a,"b is ",b,"c is ",c,)
            if b and C and c is not None:
               B=sin((radians(b))*C)/sin(radians(c))
               print("A is ",A,"B is ",B,"C is ",C,"a is ",a,"b is ",b,"c is ",c,)
        if C is None:
            if b and A and a is not None:
                C=sin((radians(c))*A)/sin(radians(a))
                print("A is ",A,"B is ",B,"C is ",C,"a is ",a,"b is ",b,"c is ",c,)
            if b and C and c is not None:
                C=sin((radians(c))*B)/sin(radians(b))
                print("A is ",A,"B is ",B,"C is ",C,"a is ",a,"b is ",b,"c is ",c,)
    elif solve is "angle" is True
        if a is None:
            if A and B and b is not None:
                a=arcsin((radians(b)*A)/B)
                print("A is ",A,"B is ",B,"C is ",C,"a is ",a,"b is ",b,"c is ",c,)
            if A and C and c is not None:
                a=arcsin((radians(c)*A)/C)
                print("A is ",A,"B is ",B,"C is ",C,"a is ",a,"b is ",b,"c is ",c,)
        if b is None:
            if B and A and a is not None:
                b=arcsin((radians(a)*B)/A)
                print("A is ",A,"B is ",B,"C is ",C,"a is ",a,"b is ",b,"c is ",c,)
            if B and C and c is not None:  
                b=arcsin((radians(c)*B)/C)
                print("A is ",A,"B is ",B,"C is ",C,"a is ",a,"b is ",b,"c is ",c,)
        if c is None:
            if C and A and a is not None:
                c=arcsin((radians(a)*C)/A)
                print("A is ",A,"B is ",B,"C is ",C,"a is ",a,"b is ",b,"c is ",c,)
            if C and B and b is not None:
                c=arcsin((radians(b)*C)/B)
                print("A is ",A,"B is ",B,"C is ",C,"a is ",a,"b is ",b,"c is ",c,)