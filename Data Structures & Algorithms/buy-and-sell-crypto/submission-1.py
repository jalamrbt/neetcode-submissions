class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice=prices[0]
        bestProfit=0
        for value in prices:
            if value<=minPrice:
                minPrice = value
            else:
                profit = value-minPrice
                if profit>bestProfit:
                    bestProfit = profit
                 
        return bestProfit