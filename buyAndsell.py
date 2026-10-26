class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_buy=float("inf"); max_profit=0
        n=len(prices)
        for i in range(0,n):
            min_buy=min(min_buy, prices[i])
            max_profit=max(max_profit,prices[i]-min_buy)
        return max_profit        