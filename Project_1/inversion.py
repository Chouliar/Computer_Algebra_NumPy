from sympy import ZZ,floor

def extendedgcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extendedgcd(ZZ.rem(b,a), a)
        return (g,(x-(floor(ZZ.quo(b,a)*y))), y)

def inversion(a, m):
    g, x,_ = extendedgcd(a, m)
    if g != 1:
        raise Exception('Δεν υπάρχει αντίστροφος')
    else:
        return ZZ.rem(x,m)
    
    
for i in range(1,29):
    print ("Με m: "+str(i)+" και n:29\nΤο πολλαπλασιαστικό αντίστροφο είναι:" +str(inversion(i,29)) +"\n")
    
    