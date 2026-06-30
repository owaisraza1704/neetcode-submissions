class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for i in nums:
            res[i] = res.get(i,0) + 1
        sorted_keys = sorted(res.keys(), key=lambda x: res[x], reverse=True)
        return sorted_keys[:k]
        