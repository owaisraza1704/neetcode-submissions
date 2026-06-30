class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanedString = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        left = 0
        right = len(cleanedString) - 1

        while left < right:
            if cleanedString[left] != cleanedString[right]:
                return False
            left += 1
            right -= 1
        
        return True