class Solution:
    def word_count(self, word: str) -> dict:
        word_count = {}
        for char in word:
            word_count[char] = word_count.get(char,0)+1
        return word_count

    def isAnagram(self, s: str, t: str) -> bool:
        s_count = self.word_count(s)
        t_count = self.word_count(t)
        if s_count == t_count:
            return True
        else:
            return False