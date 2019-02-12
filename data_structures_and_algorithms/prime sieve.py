for _ in range(int(input())):
    m,n=map(int,input().split())

    arr=[True]*(n+1)
    arr[0]=False
    arr[1]=False

    isprime=2


    while(isprime*isprime<=n):

        if arr[isprime]:
            for i in range(isprime*2,n+1,isprime):
                arr[i]=False


        isprime+=1



    for i in range(m,n+1):
        if arr[i]==True:
            print(i)
