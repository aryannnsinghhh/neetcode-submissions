class Solution:
    def isPalindrome(self, s: str) -> bool:
        for char in s:
            if char.isalnum():
                continue
            else: s = s.replace(char,"")
        s = s.lower()
        if ''.join(reversed(s)) == s:
            return True
        return False
        