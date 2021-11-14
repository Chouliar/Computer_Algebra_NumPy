from sympy import ZZ, floor, Abs
def gcdcounter(a,b,divisions): 
    if(b==0): 
        return a,divisions
    if (a>=b):
        if ZZ.rem(a,b)<=floor(Abs(b)/2):
            return gcdcounter(b,ZZ.rem(a,b),divisions+1)
            
        else:
            if (ZZ.quo(a,b)>0):
                return gcdcounter(b,b*(ZZ.quo(a,b)+1)-a,divisions+1)
            else:
                return gcdcounter(b,b*(ZZ.quo(a,b)-1)-a,divisions+1)
    else:
        if ZZ.rem(b,a)<=floor(Abs(a)/2):
            return gcdcounter(a,ZZ.rem(b,a),divisions+1)
        else:
            if (ZZ.quo(b,a)>0):
                return gcdcounter(a,a*(ZZ.quo(b,a)+1)-b,divisions+1)
            else:
                return gcdcounter(a,a*(ZZ.quo(b,a)-1)-b,divisions+1)