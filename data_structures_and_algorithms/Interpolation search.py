#Time Complexity O(log log n) average case and O(n) worst case
#Is better than Binary Search when array elelemnts are uniformly present



arr=[1,1,2,3,4,6,7,8,10,11,12,14,16,18,20,21,22,24]
length=len(arr)
start=0
end=length-1
element=48
flag=True

while(start<=end):


    pos=start+int((element-arr[start])*(end-start)/(arr[end]-arr[start]))
    
    #print(pos,arr[pos])

    if pos>length or pos<0:
        print("Element Not Found")
        flag=False
        break

    if arr[pos]==element:
        print("Element found at index",pos)
        flag=False
        break

    if arr[pos]<element:
        start=pos+1

    if arr[pos]>element:
        end=pos-1

if flag:
    print("Element Not Found")

