from sympy import ZZ

def extendedgcd(a,b):
    
    t0,t1,s0,s1 = 0,1,1,0
    
    while a!=0:
        
        q,b,a = ZZ.quo(b,a),a,ZZ.rem(b,a)
        s0,s1 = s1,s0 - q*s1
        t0,t1 = t1,t0 - q*t1
        return b,t0,s0
    
def inversion (a,b):
    
    g,x,_ = extendedgcd(a,b)
    
    if g == 1:
        
        return ZZ.rem(x,b)
    
    else:
        
        return None