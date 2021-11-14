from sympy import floor, pi
from sympy.matrices.matrices import  *

def Cont_Fractions (float_numb):
    
    CF_list = []
    a1 = float(float_numb)
    print(a1)
    i = 0
    while i < 1000 :
        c1 = floor(a1)
        CF_list.append(c1)
        b2 = a1 - c1
        a1= 1 / b2
        i = i + 1
    print(CF_list)
