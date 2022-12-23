class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        mp={}
        for ch in list1:
            if ch in list2:
                mp[ch]=list1.index(ch)+list2.index(ch)
        return [k for k in mp.keys() if mp[k]==min(mp.values())]