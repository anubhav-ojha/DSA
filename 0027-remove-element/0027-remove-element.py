class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if val != nums[i]:
                nums[index] = nums[i]
                index += 1
        return index        
            
        