class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k > len(nums):
            return []
        res = []

        l = 0 

        for r in range(k-1,len(nums)):
            window = nums[l:r+1]
            window.sort()
            res.append(window[-1])
            l+=1

        return res