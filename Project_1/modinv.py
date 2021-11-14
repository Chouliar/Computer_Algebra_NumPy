from sympy import ZZ,floor

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(ZZ.rem(b,a), a)
        return (g,(x-(floor(ZZ.quo(b,a)*y))), y)

def modinv(a, m):
    g, x,_ = egcd(a, m)
    if g != 1:
        raise Exception('Δεν υπάρχει αντίστροφος')
    else:
        return ZZ.rem(x,m)
    
    
for i in range(1,29):
    print ("Με m: "+str(i)+" και n:29\nΤο πολλαπλασιαστικό αντίστροφο του m είναι:" +str(modinv(i,29)) +"\n")
    
    