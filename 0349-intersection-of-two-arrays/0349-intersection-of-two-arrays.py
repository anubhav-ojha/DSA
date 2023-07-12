class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        clist = []
        
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    if nums1[i] in clist:
                        continue
                    else:
                        clist.append(nums1[i])
                else:
                    continue
        return clist            