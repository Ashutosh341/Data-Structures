n = int(input())
count=n-1
for i in range(1,n+1):
    for j in range(count,0,-1):
        print(' ',end='')
    count-=1
    Increasingnum=1
    for k in range(1,i+1):
        print(Increasingnum,end='')
        Increasingnum+=1
    decreasingnum=i-1
    for l in range(2,i+1):
        print(decreasingnum,end='')
        decreasingnum-=1
    print()
