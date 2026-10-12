class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[i] <= prices[j] and profit < prices[j] - prices[i]:
                    profit = prices[j]-prices[i]
            i += 1
        return profit