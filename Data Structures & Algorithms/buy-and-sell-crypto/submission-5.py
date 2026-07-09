class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r, profit = 0, 1, 0
        n = len(prices)
        while l<=r and l<n and r<n:
            if prices[l]>prices[r]:
                l+=1
            else:
                profit = max(profit,prices[r]-prices[l])
                r+=1
        return profit