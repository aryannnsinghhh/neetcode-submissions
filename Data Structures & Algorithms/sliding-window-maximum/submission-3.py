class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = r = idx = 0
        q = collections.deque()
        result = []
        while r < len(nums):
            while q and nums[r] > q[-1]: q.pop()
            q.append(nums[r])
            
            if l > nums.index(q[0], idx): 
                idx = nums.index(q[0], idx) + 1
                q.popleft()
            if r+1 >= k:
                result.append(q[0])
                l += 1
            r += 1
        return result