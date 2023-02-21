class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        x=0
        for i in nums:
            x=x^i
        return x
        