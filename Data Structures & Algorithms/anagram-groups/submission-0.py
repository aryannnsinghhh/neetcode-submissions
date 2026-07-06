class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in seen:
                seen[sorted_word] = [word]
            else:
                seen[sorted_word].append(word)
        output = []
        for key in seen:
            output.append(seen[key])
        return output