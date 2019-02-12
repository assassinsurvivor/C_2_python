#Time Complexity O(log n)


def binary_search(l,r,element):
    flag=True
    while(l<=r):

        mid=int(l+(r-l)/2)

        if arr[mid]==element:
            flag=False
            return mid
        

        elif arr[mid]<element:
            l=mid+1

        else:
            r=mid-1

    if flag:
        return False



def expo(element,k):
    if element>arr[-1] or element<arr[0]:
        return False

    if arr[0]==element:
        return 0

    i=1

    while(i<k and arr[i]<=element):
        i=i*2
    
    
    
    return binary_search(i/2,min(i,k),element)
        

arr=[1,3,5,7,8,9,10,11,12,13,14,15]
k=len(arr)
key=3
print(expo(key,k))
