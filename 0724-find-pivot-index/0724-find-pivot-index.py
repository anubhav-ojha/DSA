class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        totalSum = sum(nums)
        numSum = 0
        for i, num in enumerate(nums):
            if totalSum - numSum *2 == num:
                return i
            numSum += num
        return -1