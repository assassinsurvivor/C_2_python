##from math import sqrt,floor
##n=int(input())
##t=floor(sqrt(n))+1
##flag=False
##
##
##
##for i in range(2,t):
##    res=n/i
##    if res==1:
##        print("yes!")
##        flag=True
##        break
##    while(res>1):
##        res=res/i
##
##    if(res==1):
##        print("YES")
##        flag=True
##        break
##if not flag:
##    print("NOOOOOOOOOOOOOOOO")
##
##
##
##better version


##from math import log,sqrt,floor
##import sys
##n=int(input())
##t=floor(sqrt(n))+1
##flag=False
##
##
##for i in range(2,t):
##    x=log(n)/log(i)
##    print(x)
##    if x-int(x)<sys.float_info.epsilon:
##        print("YESSSSSSSSSSSSS!")
##        flag=True
##        break
##
##if not flag:
##    print("Nooooooooooooooooooo!")


##from math import log,sqrt,floor
##import sys
##n=int(input())
##t=floor(sqrt(n))+1
##flag=False
##
##
##for i in range(2,t):
##    x=log(n,2)/log(i,2)
##    #print(x)
##    if x-int(x)<sys.float_info.epsilon:
##        #if int(round(n**1/x))**int(round(x))==n:
##        print("YESSSSSSSSSSSSS!")
##        flag=True
##        break
##
##if not flag:
##    print("Nooooooooooooooooooo!")
##    
import sys        
for _ in range(int(input())):
    n=int(input())
    flag=False

    i=2
    x=10

    while(x>=2 and  not flag):
        x=n**(1/i)
        

        if  x==int(x) or round(x)**i==n and x>=2:
            print(i,x)
            
            
            print("Yes!")
            flag=True
            break
        i+=1
    if not flag:
        print("No!")


    
