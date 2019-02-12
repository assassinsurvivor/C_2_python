# N-Queen's problem
def safe(board,row,col):
    for i in range(col):
        if board[row][i]==1:
            return False
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[i][j]==1:
            return False
    for i,j in zip(range(row,n,1),range(col,-1,-1)):
        if board[i][j]==1:
            return False
    return True
        
        
        
def solver(board,col):
    if col>=n:
        return True


    for i in range(n):
        if safe(board,i,col):
            board[i][col]=1
            if solver(board,col+1):
                return True
            
    
            board[i][col]=0

    
    return False

    

                

n=int(input())
board=[[0 for i in range(n)]for j in range(n)]
x=solver(board,0)
board0=[["Q" if board[i][j]==1  else "-" for i in range(n)]for j in range(n)]
for i in range(n):
        for j in range(n):
            print(board0[i][j]),
        
