class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        prev = 0
        for start in range(0, len(nums)):
            if(nums[start] != 0):
                hold = nums[start]
                nums[start] = nums[prev]
                nums[prev] = hold
                prev += 1
    
