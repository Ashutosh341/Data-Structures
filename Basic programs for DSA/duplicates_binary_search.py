def duplicates_binary_search(arr ,start,end,target):
    
    
    
    if start<=end:
        
        mid = (start+end) // 2
        
        if arr[mid] == target and arr[mid-1] != target:
            return "Element is present at index ",mid
        
        elif arr[mid] == target and arr[mid-1] == target:
            return duplicates_binary_search(arr , start ,mid-1,target)
            
            
            
            
        
        elif arr[mid] < target:
            return duplicates_binary_search(arr , mid+1 ,end,target)
        
        elif arr[mid] > target:
            return duplicates_binary_search(arr , start ,mid-1,target)
        
    return  "Element not present ", -1

arr=[1,1,1,2,44,44,44,55,55,65,65,65,65,122,150,150,150,150]
#target=150

print(duplicates_binary_search(arr ,start=0,end=len(arr)-1,target=1))
