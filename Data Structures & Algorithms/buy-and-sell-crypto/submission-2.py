class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b, s, profit = 0, 1, 0
        n = len(prices)
        while b<=s and b<n and s<n:
            buy, sell = prices[b], prices[s]
            if buy>sell:
                b+=1
                print("zyada me kharida")
            else:
                print("zyada me becha")
                profit = max(profit,sell-buy)
                print(profit)
                s+=1
        return profit