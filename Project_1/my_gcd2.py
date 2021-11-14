from sympy import ZZ

def my_gcd2(a,b,array):
    
    
    if a == 0 :
        print("\n\tΕπομένως ο μκδ("+str(array[0][1])+","+str(array[0][2])+") = "+str(array[3][3])+" το οποίο ισούτε με\n")
        array.reverse()
        temp ="\t={0}- {1}*{2}".format(array[0][1],array[0][2],array[0][3])
        print(temp)
    
        for i in range(1,len(array)):
            temp =temp.replace(str(array[i][0]),"({0} - {1}*{2})").format(array[i][1],array[i][2],array[i][3])
            print(temp)
        
            
        return (b,0,1)
    
    else:

        if ((ZZ.quo(b,a) > 0) and (ZZ.rem(b,a) > 0)) :
            temp = [ZZ.rem(b,a),b,a,ZZ.quo(b,a)]
            array.append(temp)
            
        if ZZ.quo(b,a):
            print("\t{0} ={1}*{2} + {3}".format(b,ZZ.quo(b,a),a,ZZ.rem(b,a)))
            
        g,x,y = my_gcd2(ZZ.rem(b,a),a,array)
        return (g,y-ZZ.quo(b,a)*x,x)
    
print("\nA.\n")
a = 13
b = 8
print("\t>μκδ("+str(a)+","+str(b)+");")
g,x,y = my_gcd2(a,b,[])
print("\n\tΔηλαδή s = {2} και t = {4}.\n\n\t{0} = {1}*({2}) + {3}*({4})\n\n\nB.\n".format(g,a,x,b,y))

a = 612
b = 342
print("\t>μκδ("+str(a)+","+str(b)+");")
g,x,y = my_gcd2(a,b,[])
print("\n\tΔηλαδή s = {2} και t = {4}.\n\n\t{0} = {1}*({2}) + {3}*({4})\n\n\nΓ.\n".format(g,a,x,b,y))


a = 770
b = 567
print("\t>μκδ("+str(a)+","+str(b)+");")
g,x,y = my_gcd2(a,b,[])
print("\n\tΔηλαδή s = {2} και t = {4}.\n\n\t{0} = {1}*({2}) + {3}*({4})\n\n\n".format(g,a,x,b,y))
