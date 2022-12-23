class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        mp={}
        num=0
        for i in range(len(jewels)):
            mp[jewels[i]]=i
        for i in stones:
            if i in mp:
                num+=1
        return num