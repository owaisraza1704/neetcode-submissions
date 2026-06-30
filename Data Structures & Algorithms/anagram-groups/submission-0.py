class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def isAnagram(s1,s2):
            s1Hash = {}
            s2Hash = {}
            
            for i in s1:
                s1Hash[i] = s1Hash.get(i,0) + 1
            
            for j in s2:
                s2Hash[j] = s2Hash.get(j,0) + 1
                
            return s1Hash == s2Hash
        res = []
    
        for i in strs:
            for j in range(len(res)):
                if isAnagram(i,res[j][0]):
                    res[j].append(i)
                    break
            else:
                res.append([i])
        return res