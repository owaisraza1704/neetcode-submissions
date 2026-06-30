class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        longest = 0
        for i in range(n):
            seen = set()
            count = 0
            for j in range(i, n):
                if s[j] not in seen:
                    count += 1
                    seen.add(s[j])
                else:
                    break
                longest = max(longest,count)
            
        return longest