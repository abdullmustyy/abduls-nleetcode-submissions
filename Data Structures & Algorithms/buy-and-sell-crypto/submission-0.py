class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0

        for i, n in enumerate(prices):
            w = prices[:i]

            if w:
                profit = n - min(w)

                if profit > 0:
                    ans = max(ans, profit)

        return ans