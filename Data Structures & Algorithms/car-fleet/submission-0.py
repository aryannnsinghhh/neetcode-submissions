class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p,s in zip(position, speed)]
        res = []
        for p,s in sorted(pair, reverse = True):
            if res and res[-1] >= ((target-p)/s):
                continue
            res.append((target-p)/s)
        return len(res)