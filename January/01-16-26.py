class Solution:
    def maximizeSquareArea(self, n: int, m: int, hFences: List[int], vFences: List[int]) -> int:
        #hBars and vBars have to be sorted
        hBars = sorted(hFences)
        hBars.insert(0, 1)
        hBars.append(n)

        vBars = sorted(vFences)
        vBars.insert(0,1)
        vBars.append(m)

        h_widths = set()
        v_widths = set()

        N = len(hBars)
        M = len(vBars)

        
        for i in range(N-1):
            for j in range(i+1, N):
                h_widths.add(hBars[j] - hBars[i])

        for i in range(M-1):
            for j in range(i+1, M):
                v_widths.add(vBars[j] - vBars[i])
        
        # print(h_widths)
        # print(v_widths)
        common_elements = h_widths & v_widths
        MOD = 10**9+7

        if len(common_elements)!=0:
            width = max(common_elements)
            area = width*width
            return area%MOD
        return -1


        
