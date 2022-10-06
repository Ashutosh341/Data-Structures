n = int(input())
count=1
for rows in range(1,n+1):
    for cols in range(1,rows+1):
        print(count,end=' ')
        count+=1
    print()
