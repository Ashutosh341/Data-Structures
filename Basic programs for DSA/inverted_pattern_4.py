n = int(input())
count=n-1
counter=1
for i in range(1,n+1):
    for j in range(count,0,-1):
        print(' ',end='')
    count-=1
    
    for j in range(1,counter+1):
        print('*',end='')
    counter+=2
    
    print()
