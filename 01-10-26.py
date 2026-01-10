class Solution:
    def cost(self, s1, s2, i, j, n, m):
        if i== n and j == m:
            return 0
        
        if i>=n :
            return ord(s2[j]) + self.cost(s1, s2, i, j+1, n, m)
        
        if j>=m:
            return ord(s1[i]) + self.cost(s1, s2, i+1, j, n, m)
        
        if s1[i] == s2[j]:
            return self.cost(s1, s2, i+1, j+1, n, m)
        
        cost1 = ord(s1[i]) + self.cost(s1, s2, i+1, j, n, m)
        cost2 = ord(s2[j]) + self.cost(s1, s2, i, j+1, n, m)
        return min(cost1, cost2)

    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # return self.cost(s1, s2, 0, 0, len(s1), len(s2))
        n = len(s1)
        m = len(s2)
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

        for j in range(1, m+1):
            dp[0][j] = ord(s2[j-1]) + dp[0][j-1]
        
        for i in range(1, n+1):
            dp[i][0] = ord(s1[i-1]) + dp[i-1][0]

        for i in range(1, n+1):
            for j in range(1, m+1):
                # if i==0 and j ==0: 
                #     continue
                
                # if i==0: -> shifted these to pre-fill
                #     dp[i][j] = ord(s2[j-1]) + dp[i][j-1]
                
                # elif j ==0:
                #     dp[i][j] = ord(s1[i-1]) + dp[i-1][j]
                
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                
                else:
                    #s1[i]!= s2[j]
                    dp[i][j] = min(ord(s1[i-1]) + dp[i-1][j],ord(s2[j-1]) + dp[i][j-1] )
        
        return dp[n][m]
