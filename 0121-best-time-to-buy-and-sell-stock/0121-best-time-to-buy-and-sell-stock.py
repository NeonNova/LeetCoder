class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        buy_index = 0

        for sell_index in range(1, n):
            if prices[sell_index] < prices[buy_index]:
                buy_index = sell_index
            else:
                max_profit = max(max_profit, prices[sell_index] - prices[buy_index])

        return max_profit