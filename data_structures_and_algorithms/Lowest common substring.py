



def lcs(n1,n2,str1,str2):

    dp_matrix=[[0 for i in range(n1+1)]for j in range(n2+1)]
    maxw=0

    for i in range(n2+1):
        for j in range(n1+1):
            if i==0 or j==0:
                dp_matrix[i][j]=0

            elif str2[i-1]==str1[j-1]:
                dp_matrix[i][j]=1+dp_matrix[i-1][j-1]
                if dp_matrix[i][j]>maxw:
                    maxw=dp_matrix[i][j]

    return maxw




str1="prakhar"
str2="thapak"
x=len(str1)
y=len(str2)
print(lcs(x,y,str1,str2))
