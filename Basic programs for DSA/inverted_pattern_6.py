n = int(input())
counter=n
count=1
for rows in range(1,n+1):
    for space in range(counter,0,-1):
        print('#',end='')
    counter-=1
    for cols in range(1,count+1):
        print('*',end='')
    for space in range(1,rows+1):
        print('#',end='')
    for cols in range(1,)

    print()
    count+=2
