class Solution:
    def maxArea(self, heights: List[int]) -> int:

        res = 0
        lo, hi = 0, len(heights) - 1

        while lo < hi:

            area =  min(heights[lo], heights[hi]) * (hi - lo)
            res = max(res, area)
            


            if heights[lo] < heights[hi]:
                lo += 1
            else: 
                hi -= 1

        return res
        