class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) -1 
        
            
        while low <= high:
            mid = int(( low + high )/2)
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                high = mid -1 
            elif target > nums[mid]:
                low = mid +1 
        return -1       
                
                