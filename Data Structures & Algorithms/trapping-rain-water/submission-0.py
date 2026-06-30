class Solution:
    def trap(self, arr: List[int]) -> int:
        if len(arr) < 3:
            return 0

        left, right = 0, len(arr) - 1
        left_max, right_max = arr[left], arr[right]
        trapped_water = 0

        while left < right:
            # The smaller side is the limiting wall, so we resolve that side first.
            if left_max <= right_max:
                left += 1
                left_max = max(left_max, arr[left])
                trapped_water += left_max - arr[left]
            else:
                right -= 1
                right_max = max(right_max, arr[right])
                trapped_water += right_max - arr[right]

        return trapped_water