class Solution:
    def trap(self, height: List[int]) -> int:
        vol = 0
        l, r = 0, len(height)-1
        left_max, right_max = height[l], height[r]
        while l<r:
            if left_max <= right_max:
                l+=1
                left_max = max(left_max, height[l])
                vol = vol + (left_max-height[l])
            else:
                r-=1
                right_max = max(right_max,height[r])
                vol = vol + (right_max-height[r])
        return vol