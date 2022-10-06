n=int(input())

count=n
for i in range(1,n+1):
    num=1
    for j in range(count,0,-1):
        print(num,end='')
        num+=1
        
    print()
    count-=1
'''
count=n
for i in range(1,n+1):
    
    for j in range(count,0,-1):
        print('*',end='')
        
    print()
    count-=1
'''
