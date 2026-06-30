class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "EMPTY_LIST"
        return 'ß'.join(strs)

    def decode(self, s: str) -> List[str]:

        if s == "EMPTY_LIST":
            return []
        
        return s.split('ß')
