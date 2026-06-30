class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        res = 0
        for num in nums:
            curr = num
            count = 0
            while curr in unique:
                count += 1
                curr += 1
            res = max(count, res)
        return res
