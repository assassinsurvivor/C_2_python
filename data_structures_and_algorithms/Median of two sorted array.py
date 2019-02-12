from sys import maxsize
array1=[23,26,31,35]
array2=[3,5,7,9,11,16]
arr_length1=len(array1)
arr_length2=len(array2)
res=(min(arr_length1,arr_length2))
start=0
end=res-1
partx=(start+end)//2
party=int(((arr_length1+arr_length2+1)/2))-partx
flag=True
while(flag):
    #print(partx,party)

    a= -(maxsize) if partx==0 else array1[partx-1]
    b= -(maxsize) if party==0 else array2[party-1]
    c=  (maxsize) if partx==arr_length1+1 else array1[partx]
    d=  (maxsize) if partx==arr_length2+1 else array2[party]

    if (a<=d) and (b<=c):
        total=arr_length1+arr_length2
        if total%2==0:
            ff=max(a,b)
           
            result=(ff+min(c,d))/2
            flag=False
        else:
            
            result=max(a,b)
            flag=False

    elif (a>d):
        end=partx-1
        partx=(start+end)//2
        party=int(((arr_length1+arr_length2+1)/2)-partx)

    else:
        start=partx+1
        partx=(start+end)//2
        party=int(((arr_length1+arr_length2+1)/2))-partx
        


print(result)

#for testing purpose

array=array1+array2
print(sorted(array))
        
        
        
    
