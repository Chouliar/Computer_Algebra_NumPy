from sympy import ZZ,floor

def extendedgcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, s, t = extendedgcd(ZZ.rem(b,a), a)
        return (g,(s-(floor(ZZ.quo(b,a)*t))), t)

a = 13
b = 8
g,s,t = extendedgcd(a,b)
print("ΜΚΔ των "+str(a)+" και "+str(b)+" = "+str(g)+"\ns="+str(s)+"\nt="+str(t)+"\nΑρα:\n{0} = {1}*({2}) + {3}*({4})\n".format(g,a,s,b,t))

a = 612
b = 342
g,s,t = extendedgcd(a,b)
print("ΜΚΔ των "+str(a)+" και "+str(b)+" = "+str(g)+"\ns="+str(s)+"\nt="+str(t)+"\nΑρα:\n{0} = {1}*({2}) + {3}*({4})\n".format(g,a,s,b,t))

a = 770
b = 567
g,s,t = extendedgcd(a,b)
print("ΜΚΔ των "+str(a)+" και "+str(b)+" = "+str(g)+"\ns="+str(s)+"\nt="+str(t)+"\nΑρα:\n{0} = {1}*({2}) + {3}*({4})\n".format(g,a,s,b,t))