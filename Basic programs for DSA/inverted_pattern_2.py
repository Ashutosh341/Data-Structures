n=int(input())
count=n-1

for rows in range(1,n+1):
    for space in range(count,0,-1):
        print(' ',end='')
    count-=1
    for cols in range(1,rows+1):
        print('*',end='')
    print()
