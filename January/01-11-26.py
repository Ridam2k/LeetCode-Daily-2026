class Solution:
    def getLargestHistogram(self, heights, n):
        stack = []
        i = 0
        max_area = 0

        for i in range(n):
            #cannot extend stack.top() further
            while stack and heights[i] < heights[stack[-1]]:
                height_popped = heights[stack[-1]]
                #update stack
                stack.pop()

                width = 0

                #leftmostIdx
                if stack:
                    width = i - stack[-1] -1
                else:
                    width = i
                area = height_popped * width
                max_area = max(max_area, area)

            stack.append(i)
            # print(stack)
        

        #rightmostIdx = n

        while stack:
            # i = n
            height_popped = heights[stack[-1]]
            #update stack
            stack.pop()

            width = 0

            #leftmostIdx
            if stack:
                width = n - stack[-1] -1
            else:
                width = n

            area = height_popped * width

            max_area = max(max_area, area)
        
        return max_area

    def maximalRectangle(self, mat: List[List[str]]) -> int:
        n = len(mat)
        m = len(mat[0])
        ans = 0

        arr = [0 for _ in range(m)]

        for j in range(m):
            if mat[0][j] == "1":
                arr[j]+=1
        
        # print(arr)
        ans = self.getLargestHistogram(arr, m)
        # print(ans)

        for i in range(1, n):
            for j in range(m):
                if mat[i][j] == "1":
                    arr[j]+=1
                
                else:
                    arr[j] = 0
            
            print(arr)
            area = self.getLargestHistogram(arr,m)
            ans = max(ans, area)
        
        return ans
