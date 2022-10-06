n = int(input())

for rows in range(1,n+1):
    count=rows
    for cols in range(1,rows+1):
        print(count,end=' ')
        count+=1
    print()
    
