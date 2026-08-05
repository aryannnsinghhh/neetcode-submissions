class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = heights[0]
        for i, h in enumerate(heights):
            new_index = i # initialise
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i-index))
                new_index = index
            stack.append((new_index, h))
        for idx, ht in stack:
            maxArea = max(maxArea, ht * (len(heights)-idx))
        return maxArea