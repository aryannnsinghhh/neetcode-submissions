class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]
        for i in range (1,len(nums)):
            result.append(nums[i-1] * result[i-1])
        prod = 1
        for i in range (len(result)-1,0,-1):
            prod = prod * nums[i]
            result[i-1] = result[i-1] * prod
        return result