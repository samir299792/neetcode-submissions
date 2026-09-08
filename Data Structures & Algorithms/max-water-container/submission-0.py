class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights)-1

        result = 0 

        while i < j:
            max_area = min(heights[i],heights[j])*(j-i)

            result = max(max_area, result)

            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1
        
        return result