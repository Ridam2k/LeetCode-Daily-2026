class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total = 0
        n = len(points)

        for i in range(n-1):
            p1 = points[i]
            p2 = points[i+1]

            x1 = p1[0]
            y1 = p1[1]

            x2 = p2[0]
            y2 = p2[1]

            total+= max(abs(x2-x1), abs(y2-y1))
            # print(p1, p2, total)
        
        return total

        
