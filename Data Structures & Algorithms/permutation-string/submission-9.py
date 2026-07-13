class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        matches = 0
        s1count = [0] * 26
        s2count = [0] * 26
        for i in range(len(s1)):
            s1count[ord(s1[i])-ord('a')] += 1
            s2count[ord(s2[i])-ord('a')] += 1
        for i in range(26):
            if s1count[i] == s2count[i]:
                matches += 1
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: return True
            indexr = ord(s2[r])-ord('a')
            s2count[indexr] += 1
            if s2count[indexr] == s1count[indexr]:
                matches += 1
            elif s2count[indexr] == s1count[indexr] + 1:
                matches -= 1    # agar s2count[index], s1count[index] se ek zyada hai, that means s2count[index] bas abhi hi increment hua hai 

            indexl = ord(s2[l])-ord('a')
            s2count[indexl] -= 1
            if s2count[indexl] == s1count[indexl]:
                matches += 1
            elif s2count[indexl] == s1count[indexl] - 1:
                matches -= 1    # agar s2count[index], s1count[index] se ek kam hai, that means s2count[index] bas abhi hi decrement hua hai

            if matches == 26: return True
            l += 1           
        return matches == 26