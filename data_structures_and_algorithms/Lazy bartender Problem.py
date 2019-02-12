from collections import Counter
n=int(input()) 
c=int(input()) 

lis=[]
satisfy=0


for _ in range(c):
    x=list(map(int,input().split()))
    x.pop(0)
    lis.append(x)



satisfy=0
copy=[]


while(len(lis)!=0):
    added=[]
    
    for _ in range(len(lis)):
        added+=lis[_]
    most_common,num_most_common = Counter(added).most_common(1)[0]
    
            
    
    k=most_common
    satisfy+=1
    
    
    for i in range(len(lis)):
        if k  in lis[i]:
            continue
            
        else:
            copy.append(lis[i])
            
    lis=copy
    copy=[]
print(satisfy)
        
  
