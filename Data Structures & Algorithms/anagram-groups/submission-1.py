class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i in strs:
            sortedString = ''.join(sorted(i))
            res[sortedString].append(i)
        
        return list(res.values())
            