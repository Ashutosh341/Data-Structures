n= int(input())

for rows in range(1,n+1):
    count=n
    for cols in range(1,n+1):
        print(count,end=' ')
        count-=1
        
    print()
