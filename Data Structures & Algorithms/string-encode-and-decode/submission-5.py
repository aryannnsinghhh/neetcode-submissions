class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for i in strs:
            length = len(i)
            string += f'{length}#{i}'
        print (string)
        return (string)
    def decode(self, s: str) -> List[str]:
        i = 0
        output = []
        while i<len(s):
            j = i+1
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            output.append(word)
            i = j+1+length
        return output

            
