class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = 10**4 + 1
        maxProfit = 0
        for price in prices:
            if price < minPrice:
                minPrice = price
            maxProfit = max(maxProfit, price - minPrice)
        return maxProfit