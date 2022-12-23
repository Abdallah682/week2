class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        mp={}
        for i in range(len(nums)):
            if nums[i] in mp:
                mp[nums[i]]+=1
                continue
            mp[nums[i]]=1

        return max(mp,key=mp.get)
        