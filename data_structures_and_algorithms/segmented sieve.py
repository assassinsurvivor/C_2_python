from math import pow
for _ in range(int(input())):
    m,n=map(int,input().split())
    if m<2:
        m=2
    k=int(pow(n,.5))
    

    arr=list(range((k+1)))
    arr[0]=0
    arr[1]=0

    isprime=2


    while(isprime*isprime<=k):

        if arr[isprime]:
            for i in range(isprime*2,k+1,isprime):
                arr[i]=0


        isprime+=1
    print(arr)
    

    b=list(range(m,n+1))
    for i in arr:
        if i:
            if m%i==0:
                to_start_index=0
            else:
                var=m%i
                to_start_index=i-var
            if b[to_start_index] in arr:
                to_start_index+=i
            for z in range(to_start_index,n+1-m,i):
                b[z]=0
    for i in b:
        if i:
            print(i)

    


