class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        mid = 0
        while left <= right:
            mid = (left + right)//2
            
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid -1 
            elif target > nums[mid]:
                left = mid + 1
        return -1        
            
        