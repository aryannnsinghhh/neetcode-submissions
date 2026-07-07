class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = sorted(set(nums))
        if len(s) == 0:
            return 0
        count, lcs = 1, 1
        for i in range(1,len(s)):
            if ((s[i]-s[i-1]) == 1):
                count += 1
                if lcs < count: lcs = count
            else:
                count = 1
        return lcs