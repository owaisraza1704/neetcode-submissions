class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        def twoSum(array,target,skip):
            hashset = set()
            duplets = []
            for i in range(len(array)):
                if i==skip:
                    continue
                x = target - array[i] 
                if x in hashset:
                    duplets.append([array[i],x])
                hashset.add(array[i])
            return duplets
        for i in range(len(nums)):
            duplets = twoSum(nums,-nums[i],i)
            if len(duplets) > 0:
                for j in duplets:
                    triplets = [nums[i]]
                    triplets.extend(j)
                    triplets.sort()
                    if triplets not in res:
                        res.append(triplets)
        return res
        