

n = int(input())
count=n-1
num=n

counter=1
for i in range(1,n+1):
    for j in range(2,i+1):
        print('#',end='')
    
    for k in range(counter,n+1):
        print(k,end='')
    
    # decreasingnum=2*i-1
    # for l in range(1,i+1):
    #     print(decreasingnum,end='')
    #     decreasingnum-=1
    print()
    counter+=1
count=n-2
for i in range(1,n):
    #num=n
    for j in range(count,0,-1):
        print('#',end='')
    count-=1

    
    for k in range(n-i,n+1):
        print(k,end='')
    print()
    
