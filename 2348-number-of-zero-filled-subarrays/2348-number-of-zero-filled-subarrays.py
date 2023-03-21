class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        curr = total = 0
        for i in nums:
            if i == 0 :
                curr += 1
                total += curr
            else:
                curr = 0
        return total      
        