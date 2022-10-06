n= int(input())

even_sum=0
odd_sum =0
while n>0:
    remainder = n % 10

    if remainder % 2==0:
        even_sum = even_sum + remainder
    else:
        odd_sum = odd_sum + remainder
    n=n//10

print(even_sum , odd_sum)
