class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp={}
        mp2={}
        listt=[]
        for i in range(len(nums1)):
            mp[nums1[i]]=i
        for i in range(len(nums2)):
            if nums2[i] in mp:
                if nums2[i]in mp2:
                    continue
                listt.append(nums2[i])
            mp2[nums2[i]]=i
        return listt
