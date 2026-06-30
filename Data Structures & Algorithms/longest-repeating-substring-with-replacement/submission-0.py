class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0,0
        maxF = 0 
        res = 0
        
        while r < len(s):
            window = (r - l) + 1
            # one liner function to get the highest frequency element from the current window
            maxFrequency = max(Counter(list(s[l:r+1])).values())
            maxF = max(maxF, maxFrequency)
            if window - maxF <= k:
                res = max(res,window)
            else:
                l+= 1
            r+= 1
        
        return res