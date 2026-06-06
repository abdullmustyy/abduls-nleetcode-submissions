class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]

        for n in prices:
            profit = n - min_price
            max_profit = max(max_profit, profit)
            min_price = min(min_price, n)

        return max_profit