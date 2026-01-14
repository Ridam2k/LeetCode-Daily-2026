class Solution:
  def getArea(self, y_mid, sq):
     x = sq[0]
     y0 = sq[1]
     length = sq[2]
    #For rectangle area -> x length = length; we'll compute the width/height
     width = max( min(y_mid - y0, length), 0)
    #Case1: w = y_mid - y0 -> normal case
    #case2: w = no overlap with y_mid line and compeltely below -> Length and y_mid-y0 would be a greater incorrect value
    #case3: w = no overlap beause sq completely above the y_mid line => area contribution is 0 => y_mid-y0 would be a large incorrect negatve value
    return width * length
    
    def separateSquares(self, squares: List[List[int]]) -> float:
      ## Binary Search for finding the min y-line
      n = len(sqaures)
      low = sys.maxsize
      high = -sys.maxsize

      totalArea = 0

      for sq in squares:
        x = sq[0]
        y = sq[1]
        length = sq[2]
        
        low = min(low, y)
        high = max(high, y + length)
        
        totalArea++ length*length

      #Now we have our bounds for the binary search
      while (high - low) > 1e-6:
        #i.e. if high ~ low we break
        y_mid = (low+high)/2
        areaBelow =0
        
        for sq in squares:
          areaBelow+=  self.getArea(y_mid, sq)
          
        areaAbove = totalArea/2
        
        if areaBelow < areaAbove:
          low = y_mid
        else:
          high = y_mid

      return low
        
      
