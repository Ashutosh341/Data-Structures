s= int(input())
e= int(input())
w= int(input())

import math
celcius=0 
for i in range(s,e+1,w):
    
    celcius = (i - 32) * 5/9
    print(i, math.ceil(celcius),'\n')
    #s=s+20
