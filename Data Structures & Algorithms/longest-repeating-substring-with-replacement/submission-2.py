class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxF= 0
        res = 0
        count = Counter()
        
        for r in range(len(s)):
            count[s[r]] += 1
            
            maxF = max(maxF, count[s[r]])
            
            window = (r-l) + 1
            
            if window - maxF > k:
                count[s[l]] -= 1
                l += 1
            else:
                res = max(res,window)
        return res