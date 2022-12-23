class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        ans = s1.split() + s2.split()
        dt = {}
        for x in ans:
            if x not in dt:
                dt[x] = 1
            else:
                dt[x] +=1
                
        arr = []
        for x in dt.keys():
            if dt[x] == 1:
                arr.append(x)
                
        return arr