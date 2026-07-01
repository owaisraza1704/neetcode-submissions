class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_hash = {}
        s2_hash = {}
        l = 0
        
        for i in range(len(s1)):
            s1_hash[s1[i]] = s1_hash.get(s1[i],0) + 1
            
            s2_hash[s2[i]] = s2_hash.get(s2[i],0) + 1
        
        for r in range(len(s1),len(s2)):
            
            if s1_hash == s2_hash : 
                return True
            
            s2_hash[s2[r]] = s2_hash.get(s2[r],0) + 1
            
            s2_hash[s2[l]] = s2_hash.get(s2[l]) - 1
            if s2_hash.get(s2[l]) == 0:
                s2_hash.pop(s2[l])
            l += 1
            
        return s1_hash == s2_hash