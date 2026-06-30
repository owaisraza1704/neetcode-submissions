class Solution:
    def isAnagram(self,s: str, t: str) -> bool:
        shash={}
        thash={}

        for i in s:
            shash[i] = shash.get(i, 0) + 1
        for i in t:
            thash[i] = thash.get(i, 0) + 1
            
        return shash == thash