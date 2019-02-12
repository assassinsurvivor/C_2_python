#Binary Search
#Time complexity
#Best case -> O(1)
#Worst case -> O(log(n))

arr=[1,3,5,7,9,10,11,13,15,17,19]
element=11
start=0
flag=True
end=len(arr)-1
while(start<=end):
    mid=start+(end-start)//2
    if arr[mid]==element:
        print("Yeahhhhhhh! element is at index", mid)
        flag=False
        break
    elif arr[mid]>element:
        end=mid-1
    elif arr[mid]<element:
        start=mid+1
if flag:
    print("Element is not in the list :( ")
    



#If want to search for first occurence of the element in the list then when arr[mid]==element
#change end =mid-1 and for last occurence change start=mid+1 while terminating condition remains the same
print("##################################################################")

arr=[1,3,5,7,11,11,11,13,15,17,19]
element=11
start=0
flag=True
store_index=0
end=len(arr)-1
while(start<=end):
    mid=start+(end-start)//2
    if arr[mid]==element:
        store_index=mid
        end=mid-1
        flag=False
        
    elif arr[mid]>element:
        end=mid-1
    elif arr[mid]<element:
        start=mid+1
if flag:
    print("Element is not in the list :( ")

else:
    print("Yeahhhhhhh! element is at index", store_index)
    
