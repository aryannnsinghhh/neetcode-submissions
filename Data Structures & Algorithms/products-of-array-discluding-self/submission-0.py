class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range (0,len(nums)):
            prod = 1
            for j in range (0, len(nums)):
                if i != j:
                    prod = prod * nums[j]
            result.append(prod)
        return result