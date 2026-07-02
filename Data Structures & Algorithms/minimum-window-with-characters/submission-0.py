class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s1_hash = {}
        for i in range(len(s)):
            s1_hash[s[i]] = i
        
        indexes = []
        
        for string in t:
            if string not in s1_hash:
                return ""
            indexes.append(s1_hash[string])
        
        indexes.sort()
        minIdx = indexes[0]
        maxIdx = indexes[-1]
        return s[minIdx:maxIdx+1]