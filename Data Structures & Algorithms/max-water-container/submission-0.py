class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left , right = 0 , len(heights) - 1
        mostWater = 0
        while left < right:
            mostWater = max(mostWater, min(heights[left],heights[right]) * (right - left))

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return mostWater