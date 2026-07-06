class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            seen[num] = seen.get(num,0) + 1
        most_freq = []
        while len(most_freq) < k:
            max = 0
            for num in seen:
                print (num, max)
                if max < seen[num]:
                    max = seen[num]
                    add = num
            most_freq.append(add)
            del seen[add]
        return most_freq