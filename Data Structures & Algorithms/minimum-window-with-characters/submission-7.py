class Solution:
    def make_dict(self, s: str) -> dict:
        output = {}
        for word in s:
            output[word] = 1 + output.get(word,0)
        return output
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""
        elif len(s)==len(t): 
            return s if sorted(s) == sorted(t) else ""
        else:
            tCount = self.make_dict(t)
            tSet = set(t)
            sCount = {}
            need = len(tCount)
            have = 0
            length = float('inf')
            final = [0,0]
            l = 0
            found_match = False
            for r in range (len(s)):
                if s[r] in tSet:
                    sCount[s[r]] = 1 + sCount.get(s[r],0)
                    if sCount[s[r]] == tCount[s[r]]: have += 1
                print(sCount, have, tCount)                
                while have == need:
                    if r-l+1 < length:
                        length = r-l+1
                        final[0],final[1] = l,r
                    found_match = True
                    
                    if s[l] in tSet:
                        sCount[s[l]] -= 1
                        if sCount[s[l]] < tCount[s[l]]: have -= 1
                    l+=1
                print(final, length)
            return s[final[0]:final[1]+1] if found_match else ""

