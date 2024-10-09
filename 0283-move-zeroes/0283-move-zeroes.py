class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first = 0

        for i in range(0, len(nums)):
            if(nums[i] != 0):
                nums[first], nums[i] = nums[i], nums[first]
                first += 1
            

        