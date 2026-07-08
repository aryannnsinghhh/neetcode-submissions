class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        vol = 0
        right = len(heights)-1
        while left<right:
            if heights[left] < heights[right]:
                area = heights[left] * (right - left)
                if area > vol:
                    vol = area
                left += 1
            elif heights[right] < heights[left]:
                area = heights[right] * (right - left)
                if area > vol:
                    vol = area
                right -= 1
            else:
                area = heights[left] * (right - left)
                if area > vol:
                    vol = area
                if heights[left+1] < heights[right-1]:
                    right -= 1
                elif heights[right] < heights[left]:
                    left += 1
                else:
                    left += 1
                    right -= 1

        return vol