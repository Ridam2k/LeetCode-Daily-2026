class Solution:
    def lcs(self, nums):
        mp = set(nums)
        ans = 0

        for num in mp:
            if num-1 in mp:
                continue
            
            cnt = 1
            while num+1 in mp:
                cnt+=1
                num+=1 
            
            ans = max(ans, cnt)
        
        return ans

    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hLen = self.lcs(hBars)
        vLen = self.lcs(vBars)

        length = min(hLen, vLen)+1

        return length*length
        
