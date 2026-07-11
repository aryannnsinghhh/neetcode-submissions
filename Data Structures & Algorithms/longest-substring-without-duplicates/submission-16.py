class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ls, start = 0, 0
        seen = set()
        for end in range(len(s)):
            while s[end] in seen:
                seen.discard(s[start])
                start+=1
            seen.add(s[end])
            ls = max(ls, end - start + 1)
        return ls