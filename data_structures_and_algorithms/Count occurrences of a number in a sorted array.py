def bs(element,flag):
    low=0
    high=length-1
    index=0
    flagger=False
    

    while(low<=high):


        mid=int(low+(high-low)/2)

        if arr[mid]==element:
            index=mid
            flagger=True
            if flag==True:
                high=mid-1
            if flag==False:
                low=mid+1


        elif arr[mid]<element:
            low=mid+1

        else:
            high=mid-1
    
    return index if flagger else -1
            
arr=[1,1,2,2,2,3,3,3,3,4,4,4,4,4,5,5,5,5,5,5,6,6,6,6,6,6,6,7]
length=len(arr)
t=7
x=bs(t,True)

if x==-1:
    print("No such element exist")
if x!=-1:
    y=bs(t,False)
    
    print("Total No of times element",t,"occurs in the list is ",y-x+1)
