class Solution:

    def encode(self, strs: List[str]) -> str:
        sizes,res = [],[]

        for i in strs:
            sizes.append(len(i))

        for sz in sizes:
            res.append(str(sz))
            res.append(",")

        res.append("ß")
        res.extend(strs)
        return ''.join(res)
# "4,4,4,3,#neetcodeloveyou"
    def decode(self, s: str) -> List[str]:
        sizes= (s.split("ß")[0]).split(',')[:-1]
        string = s.split("ß")[1]
        res = []
        
        startIdx = 0
        
        for i in sizes:
            res.append(string[startIdx:startIdx+int(i)])
            startIdx += int(i)
        return res

