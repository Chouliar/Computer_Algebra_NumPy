from sympy.polys.subresultants_qq_zz import *
from sympy.polys import *
from sympy import symbols, rem, pprint, Matrix, zeros
from sympy.matrices.matrices import  *



def euclid_triang(f, g, x):
    
    #vathmos polyonimou
    d = degree(f, x)
    euclid_t_list = []
    euclid_t_list.append(f)
    euclid_t_list.append(g)
    m1 = poltoMatrix(f,g)
    
    endpoint = len(m1)
    
    while endpoint > 9 :
        
        mPivot = my_pivot(m1, 0, 0)
        mPivot2 = my_pivot(mPivot, 1, 1)
        d = ZZ.quo(len(mPivot2), 3)
        prs = rowToPol(mPivot2,d,2)
        euclid_t_list.append(prs)
        
        if len(mPivot2) > 9:
            fnew = rowToPol(mPivot2,d,1)
            gnew = rowToPol(mPivot2,d,2)
            d = d - 1
            m1 = poltoMatrix(fnew,gnew)
        
        endpoint = len(mPivot2)
        
    print(euclid_t_list)
        



def my_pivot(m, row, col):
    
    d = ZZ.quo(len(m), 3)
    x = symbols('x')
    firstRow = rowToPol(m,d,0)
    middleRow = rowToPol(m,d,1)
    lastRow = rowToPol(m,d,2)
    
    
    
   
    if row == 0 and col ==0 :
        rmnt = rem_z(lastRow, firstRow, x)
        
    else :
        
        rmnt = rem_z(lastRow, middleRow, x)
    m = poltoMatrix(rmnt,middleRow)
    return(m)
        
    
#metatrepei mia seira toy pinaka m se polyonymo    
def rowToPol(m,d,row):
    i=0;gN="";last = 0
    while i < d:
        if i != d-1 :
            if i != d-2:
                if m[row, i] < 0:    
                    s = str(-1*m[row, i])+"*x**"+str(d-i-1);pros = -1
                else:
                    s = str(m[row, i])+"*x**"+str(d-i-1);pros = 1
            else :
                if m[row, i] < 0:
                    s = str(-1*m[row, i])+"*x";pros = -1
                else:
                    s = str(m[row, i])+"*x";pros = 1
            i = i+1
        else :
            if m[row, i] < 0:
                s = str(-1*m[row, i])
                pros = -1;last = 1
            else:
                s = str(m[row, i])
                pros = 1;last = 1
            if pros == -1:
                gN = gN +" - "+ s
            else:
                gN = gN +" + "+ s
            i=i+1
        
        if i == 1 :
            if pros == -1:
                gN = " - "+ s
            else:
                gN = s
               
        else:
            if last != 1 :
                if pros == -1:
                    gN = gN +" - "+ s
                else:
                    gN = gN +" + "+ s
    f = eval(gN)
    return f

#metatrepei polyonyma se pinaka
def poltoMatrix(f,g):
    
    df = degree(f, x)
    dg = degree(g, x)
    #dhmiourgia pinakon me stoixeia polyonimon
    fM = Matrix(1, df+1, Poly(f, x).all_coeffs())
    gM = Matrix(1, dg+1, Poly(g, x).all_coeffs())
    
    #dimioyrgia g vathmou f
    mG = zeros(1,1)
    mG1 = gM.col_insert(dg+1,mG)
    mG2 = gM.col_insert(0,mG)
    m1 = mG1
    m1 = m1.row_insert(1, mG2)
  
    if df == dg:
        
        fM=fM.col_insert(0,mG)
        
    if df < dg:
        for i in range(2):
            fM=fM.col_insert(0,mG)
            i = i + 1
        i = 0
            
        
    m1 = m1.row_insert(2, fM)
    return(m1)
