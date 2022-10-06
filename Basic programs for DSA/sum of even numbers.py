N = int(input("Enter Number : "))

total=0

#Approach 2
for i in range(0,N):
    if i%2==0:
        total+=i
    else:
        continue
print(total)

"""
#Approach 1
for i in range(2,N,2): # takes a step of 2 for even numbers
    total = total +i
print(total)
"""
