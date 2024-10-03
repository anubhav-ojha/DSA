class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        runSum = [0] * len(nums)
        runSum[0] = nums[0]
        for i in range(1, len(nums)):
            runSum[i] =  nums[i] + runSum[i-1]
        
        return runSum