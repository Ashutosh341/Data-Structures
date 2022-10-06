

def prime(number):
    flag = False
    for i in range(2,number-1):
        if number%i==0:
            flag = True
    if flag:
        return 'not Prime'
    else:
        return 'Prime'
print(prime(7))


