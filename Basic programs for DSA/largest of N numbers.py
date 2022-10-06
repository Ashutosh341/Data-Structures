list1=[10,5,11,49,5,6,12,23,45]

largest =1

for i in range(0,len(list1)):
    

    if list1[i] > largest:
        largest=list1[i]
    else:
        continue
print(largest)
    

