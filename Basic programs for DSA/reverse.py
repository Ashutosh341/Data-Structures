#Write Your Code Here
#n= int(input())
n=145000
temp = 0
while (n > 0):
    remainder = n % 10
    temp = (temp * 10) + remainder
    n = n // 10

print(temp)
