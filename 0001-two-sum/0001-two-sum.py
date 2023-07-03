class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        i = 0
        while True :
            for j in range(i+1, len(nums)):
                if nums[j] == target - nums[i] :
                    return [i,j]
            i += 1
            

        