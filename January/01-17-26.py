class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        x_len = 0
        y_len = 0
        n = len(bottomLeft)
        max_len = 0

        for i in range(n):
            for j in range(i+1, n):
                i1_bl = bottomLeft[i]
                i2_bl = bottomLeft[j]

                i1_tr = topRight[i]
                i2_tr = topRight[j]

                x_start = max(i1_bl[0], i2_bl[0])
                x_end = min(i1_tr[0], i2_tr[0])

                x_len = x_end-x_start
                # print(x_len)

                y_start = max(i1_bl[1], i2_bl[1])
                y_end = min(i1_tr[1], i2_tr[1])

                y_len = y_end-y_start
                # print(y_len)

                length = min(x_len, y_len)
                max_len = max(max_len, length)
                # print(max_len)
        
        # length = min(x_len, y_len)
        # print(x_len, y_len, length)
        area = max_len*max_len
        return area

        
        


        
