from sympy import ZZ
from sympy.matrices.matrices import  *
from fractions import Fraction

Cf_list = []
def new_euclid(klasma):
    
    klasma = klasma.replace("/", " ")
    klasma = klasma.split(" ")
    a = int( klasma[0])
    b = int(klasma[1])
    
    print(a)
    print(b)
    Cf_list = CF_euclid(a,b)
    print(Cf_list)

def CF_euclid(a, b):
    
    if b > a:
        return CF_euclid(b, a)

    if (ZZ.rem(a, b)) == 0:
        Cf_list.append((ZZ.quo(a,b)))
        return Cf_list

    Cf_list.append((ZZ.quo(a,b)))
    return CF_euclid(b, (ZZ.rem(a, b)))