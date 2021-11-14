from sympy import symbols, pprint
from sympy.polys import *

x = symbols('x')

def K_method (f):
    d = degree(f,x)
    Coef_list = []
    Neg_list = []
    Coef_list = Poly(f, x).coeffs()
    i = d
    Neg_el = 0
        while i >= 0 :
            if Coef_list[i] < 0:
            Neg_list.append(Coef_list[i])
            Neg_el = Neg_el + 1
            else :
            Neg_list.append(0)
            i = i - 1
            
        for i in range (Neg_el):
            k = d - i
            rtn = (((-Neg_list[i])/(Coef_list[0]*2**(-k)))**(1/k))
    print("The upper bound is: ")
    print(float(rtn))
