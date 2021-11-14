import timeit
from sympy import symbols
from sympy.polys import *
from sympy.polys.dispersion import *
from sympy.matrices.matrices import  *
from sympy.solvers import *
from sympy import *


x = symbols('x')
lim_list = []
root_list = []
lim_list2 = []
lim_list3 = []

#---------------------------------------------------   
#euresi ano oriou
def upperbound(f):
    
    fspace = [[],[]]
    fspace=intervals(f)
    d = degree(f,x)
    
    for i in range (d):
        for j in range (1):
            oria = str(fspace[i][j])
            oria = oria.replace("(", "")
            oria = oria.replace(")", "")
            oria = oria.replace(" ", "")
            oria = oria.split(",")
    
    oria = str(oria)
    oria = oria.replace(","," ")
    oria = oria.replace("'","")
    oria = oria.replace("[","")
    oria = oria.replace("]"," ")
    oria = oria.split(" ")
    ub1 = int(oria[2])
    return (ub1)

#-----------------------------------------------------------    
#ypologismos allagon prosimoy
def sighChanges(InList):
 
    length = len(InList)
    prev = 0
    changes = 0
    
    for i in range (length): 
        if InList[i] < 0: 
            signof = -1
        else: 
            signof = +1 
      
        if signof == -prev: 
            changes = changes + 1
            prev = signof
        else:
            prev = signof
       
    return(changes)
#----------------------------------------------------------
def VAG(f,a,b):
    
    d = degree(f,x)
    vari = 0
    coeffs_list = []
    
    fvar = ((x + 1)**d * f.subs({x : (a + b*x)/(x + 1)})).simplify()
    coeffs_list = Poly(fvar,x).all_coeffs()
    vari = sighChanges(coeffs_list)
    
    if vari == 0 :
        return 
    elif vari == 1 :
        lim_list2.append([a,b])
        return
    
    m = expand((a + b)/ 2).simplify()
    
    fm = expand((f.subs({x : m})).simplify())
    if fm != 0 :
        newb = m 
        VAG(f ,a,newb)
        newa = m
        VAG(f ,newa,b)
        
#---------------------------------------------------------

# def VAS(fz,fM):
#     
#     d = degree(f,x)
#     vari = 0
#     coeffs_list = []
#     
#     coeffs_list = Poly(fz,x).all_coeffs()
#     vari = sighChanges(coeffs_list)
#     if vari == 0 :
#         return 
#     elif vari == 1 :
#         a = expand((fM.subs({x : 0})).simplify())
#         b = upperbound(fM)
#         lim_list3.append([a,b])
#         return
#     lb = lowerbound(fz)
#     print(lb)
#     if lb >=1 :
#         fz = expand((fz.subs({x : x + 1})).simplify())
#         fM = expand((fM.subs({x : x + lb})).simplify())
#         
#     p01 = expand(((x+1)**d * fz.subs({x : 1 /(x + 1)})).simplify())
#     M01  = expand((fM.subs({x : 1 /(x + 1)})).simplify())
#     m = expand((fM.subs({x : 1})).simplify())
#     p1ap = expand((fz.subs({x : (x+1) })).simplify())
#     M1ap = expand((fM.subs({x : (x+1)})).simplify())
#     p1 = expand((fz.subs({x : 1})).simplify())
#     if p1ap != 0 :
#         VAS(p01,M01)
#         VAS(p1ap ,M1ap)
#         
#     


#---------------------------------------------------------

def VCA(f,a,b):
    
    d = degree(f,x)
    vari = 0
    coeffs_list = []
    
    fvar = ((x + 1)**d * f.subs({x : 1 / (x + 1)})).simplify()
    
    coeffs_list = Poly(fvar,x).all_coeffs()
    vari = sighChanges(coeffs_list)
    m = expand((a + b)/ 2).simplify()
    
    if vari == 0 :
        return 
    elif vari == 1 :
        lim_list.append([a,b])
        return 
        
    f0_12 = expand((2**d * f.subs({x : x / 2})).simplify())
    
    f12_1 = expand((2**d * f.subs({x : (x + 1) / 2})).simplify())
    
    f1_2 = expand((f12_1.subs({x : 1/2})).simplify())
    
    if f1_2 != 0 :
        
        newb = m 
        VCA(f0_12,a,newb)
        newa = m
        VCA(f12_1 ,newa,b)
    
#---------------------------------------------------------
def findroots(foz,listoo):
  
    length = len(listoo)
    i = 0
    
    while i < length :
        interval = listoo[i]
        interval = str(interval)
        interval = interval.replace("[", "")
        interval = interval.replace("]", "")
        interval = interval.replace(" ", "")
        interval = interval.split(",")
   
        a = float(interval[0])
        
        b = float(interval[1])
        
        while (b-a)/2.0 >= 0.0000001:
            
            middle = (a + b) /2.0
            fm = expand((foz.subs({x : middle})))
            fa = expand((foz.subs({x : a})))
            if fm == 0:
                root_list.append(middle)
            elif (fm * fa) < 0:
                b = middle
            
            else :
                a = middle
                
        root_list.append(middle)
        i = i+1
                        
    

#---------------------------------------------------------
def VCA_method(fz):
    ub = upperbound(fz)
    lb = 0
    fvca = (fz.subs({x : ub*x})).simplify()
    
    start = timeit.default_timer()
    VCA(fvca,lb,ub)
    stop = timeit.default_timer()
    
    start2 = timeit.default_timer()
    VAG(fz,lb,ub)
    stop2 = timeit.default_timer()
    
#     start3 = timeit.default_timer()
#     M = x
#     VAS(fz,M)
#     stop3 = timeit.default_timer()
    
    start1 = timeit.default_timer()
    findroots(fz,lim_list)
    stop1 = timeit.default_timer()
    
    print("Method VCA:")
    print("Time of VCA to find intervals (seconds): ", stop-start)
    print("\nMethod VAG:")
    print("Time of VAG to find intervals (seconds):", stop2-start2)
#     print("\nMethod VAS:")
#     print("Time of VAS to find intervals (seconds): ", stop3-start3)
#     
    
    print("\nThe roots with 10^-6 tolerance is:",root_list)
    print('Calculating time to find positive roots (seconds): ', stop1-start1)

    
    


