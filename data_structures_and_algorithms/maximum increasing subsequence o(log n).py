#https://www.codechef.com/problems/PEC005
from sys import maxsize
for _ in range(int(input())):
    n=input()
    arr=list(map(int,input().split()))
    
    lis=[-maxsize]
    pointer=0

    for i in arr:

        if i>=lis[pointer]:
            lis.append(i)
            pointer+=1

        else:
            start=1
            end=pointer
            while(start<=end):
                mid= (start+end)//2

                if lis[mid]<i:
                    start=mid+1
                else:
                    end=mid-1
            lis[start]=i
    #print(lis)

    print(len(lis)-1)
