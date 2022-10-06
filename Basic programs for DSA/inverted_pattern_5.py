n = int(input())
count=n-1
for i in range(1,n+1):
    for j in range(count,0,-1):
        print(' ',end='')
    count-=1
    Increasingnum=i
    for k in range(1,i+1):
        print(Increasingnum,end='')
        Increasingnum+=1
    decreasingnum=2*i-2
    for l in range(2,i+1):
        print(decreasingnum,end='')
        decreasingnum-=1
    print()

###1
##23
#345
#4567
