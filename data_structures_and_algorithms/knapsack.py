#Recursive O(2**n)

def recursive(total,wt,n):

    if n==0 or total==0:
        return 0

    elif wt[n-1]>total:

        return recursive(total,wt,n-1)

    else:

        return max(val[n-1]+recursive(total-wt[n-1],wt,n-1),recursive(total,wt,n-1))
    

val = [60, 100, 120]
wt = [10, 20, 30]
n=len(val)
t=50
print(recursive(t,wt,n))


#DP O(n*capacity of knapsack)
#we make a dp table till range of total capacity


def knapsack(total,wt,n):


    dp=[[0 for i in range(total)]for j in range(n)]

    for i in range(n):
        for j in range(total):

            if i==0 or j==0:
                dp[i][j]=0

            elif wt[i]>j:
                dp[i][j]=dp[i-1][j]

            else:
                dp[i][j]=max(dp[i-1][j],val[i-1]+dp[i-1][j-wt[i-1]])
    return dp[n][total]

val = [60, 100, 120]
wt = [10, 20, 30]
n=len(val)
t=40
print(recursive(t,wt,n))
