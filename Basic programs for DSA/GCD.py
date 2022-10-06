

def gcd(a,b):
    if a<b:
        smaller = a
    else:
        smaller = b

        
    if smaller == a:
        if b%a==0:
            print("HCF",a)
    if smaller==b:
        if a%b==0:
            print("HCF",b)

    
    for i in range(2,smaller+1):
        if a%i==0 and b%i==0:
            hcf=i
    return hcf
            

result=gcd(12,28)
print(result)
