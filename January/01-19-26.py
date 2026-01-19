class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:

        n = len(mat)
        m = len(mat[0])

        prefixSum = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                prefixSum[i][j]+= mat[i][j]
                if i!= 0:
                  prefixSum[i][j]+= prefixSum[i-1][j]  
                if j != 0:
                   prefixSum[i][j]+= prefixSum[i][j-1]
                
                if i!=0 and j!=0:
                    prefixSum[i][j] -= prefixSum[i-1][j-1]
               
        
        # print(prefixSum)

        # for length in range(min(n,m), 0, -1):
        #     for i in range(0,n-length+1,1):
        #         for j in range(0,m-length+1, 1):
        #             # for square starting at (i,j)
        #             r = i+length-1
        #             c = j+length-1
        #             totalSum = prefixSum[r][c]
        #             if i!=0:
        #                 totalSum -= prefixSum[i-1][c]
        #             if j!=0:
        #                 totalSum-= prefixSum[r][j-1]
        #             if i!=0 and j!=0:
        #                 totalSum+= prefixSum[i-1][j-1]
                    
        #             if totalSum <= threshold:
        #                 return length
        
        #BinarySearch approach
        low = 0
        high = min(n,m)
        length = 0  #mid
        ans = 0

        while(low<=high):
            length = (low+high)//2

            found = False
            
            for i in range(0,n-length+1,1):
                for j in range(0,m-length+1, 1):
                    
                    # for square starting at (i,j)
                    r = i+length-1
                    c = j+length-1
                    totalSum = prefixSum[r][c]
                    if i!=0:
                        totalSum -= prefixSum[i-1][c]
                    if j!=0:
                        totalSum-= prefixSum[r][j-1]
                    if i!=0 and j!=0:
                        totalSum+= prefixSum[i-1][j-1]
                    
                    if totalSum <= threshold:
                        found = True
            
            if found:
                ans = length #store max len found till now
                low = length+1
            else: 
                high = length-1

        
        return ans

        
