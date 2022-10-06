list1=[3,6,9,12,4,5,7]


for i in range(0,len(list1)-1,2):
    #print('list1 1st',list1[i])
    #print('list1 12nd',list1[i+1])
    list1[i] , list1[i+1] = list1[i+1] , list1[i]

print(list1)
