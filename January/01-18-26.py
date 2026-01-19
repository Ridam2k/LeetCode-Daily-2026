class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        rowSum = [[0 for _ in range(m)] for _ in range(n)]
        colSum = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if j == 0:
                    rowSum[i][j] = grid[i][j]
                
                else:
                    rowSum[i][j] = grid[i][j] + rowSum[i][j-1]

        
        for j in range(m):
            for i in range(n):
                if i == 0:
                    colSum[i][j] = grid[i][j]
                
                else:
                    colSum[i][j] = grid[i][j] + colSum[i-1][j]
        
        # print(rowSum)
        # print(colSum)

        # ans = 0
        for length in range(min(n,m), 1, -1):
            for i in range(0, n-length+1,1):   
                for j in range(0, m-length+1, 1):
                    #For one square starting at (i, j)
                    targetSum = -1
                    if j!=0:
                        targetSum = rowSum[i][j+length-1] - rowSum[i][j-1]
                    else:
                        targetSum = rowSum[i][j+length-1]
                    
                    allSum = True
                    for row in range(i+1, i+length,1):
                        if j==0:
                            row_sum = rowSum[row][j+length-1]
                        else:
                            row_sum = rowSum[row][j+length-1] - rowSum[row][j-1]
                        if row_sum!= targetSum:
                            allSum = False
                            break
                    
                    if not allSum:
                        #next square
                        continue
            
                    for col in range(j, j+length,1 ):
                        if i == 0:
                            col_sum = colSum[i+length-1][col]
                        
                        else:
                            col_sum = colSum[i+length-1][col] - colSum[i-1][col]

                        if col_sum!= targetSum:
                            allSum = False
                            break
                    
                    if not allSum:
                        #nextSquare
                        continue
                    
                    diagSum = 0
                    antiDiagSum = 0
                    for k in range(length):
                        diagSum+= grid[i+k][j+k]
                        antiDiagSum += grid[i+k][j+length-1-k]
                    
                    if diagSum == targetSum and antiDiagSum == targetSum:
                        return length


        return 1

        
