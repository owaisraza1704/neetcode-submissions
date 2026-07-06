class Solution:
    def isValid(self, s: str) -> bool:
        closingBracket = {
            '}':'{',
            ']':'[',
            ')':'('
        }

        stack = []

        for c in s:
            if c in closingBracket:
                if stack and stack[-1] == closingBracket[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
            