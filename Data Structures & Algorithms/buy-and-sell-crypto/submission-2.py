class Solution:
    def maxProfit(self, arr: List[int]) -> int:
        lowest = arr[0]

        maxP = 0

        for price in arr:
            lowest = min(lowest, price)
            maxP = max(maxP, price - lowest)
        return maxP
