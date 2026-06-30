class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        temp=[0] * len(nums)
        for i in range(len(nums)):
            product=1
            for j in range(len(nums)):
                if i != j:
                    product *= nums[j]
            temp[i] = product
        return temp