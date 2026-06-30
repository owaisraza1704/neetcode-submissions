class Solution:
    def maxProfit(self, arr: List[int]) -> int:
        left, right = 0,1
        profit = 0
        while right < len(arr):
            if arr[left] < arr[right]:
                profit = max(profit, arr[right] - arr[left])
            else:
                left = right
            right += 1
        return profit