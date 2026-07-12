class Solution:
    def make_dic(self, a: str) -> dict:
        dic = {}
        for word in a:
            dic[word] = 1+dic.get(word,0)
        return dic
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        l = 0
        seen = {}
        for r in range (len(s2)):
            if sum(seen.values()) < k:
                seen[s2[r]] = 1+seen.get(s2[r],0)
                if seen == self.make_dic(s1):
                    return True 
            else:
                seen[s2[l]] -= 1
                if seen[s2[l]] == 0:
                    del seen[s2[l]]
                l += 1
                seen[s2[r]] = 1 + seen.get(s2[r],0)
                if seen == self.make_dic(s1):
                    return True    
        return False