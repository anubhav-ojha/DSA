class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        for i in range(len(arr)):
            if arr[i+1 ] > arr[i]:
                continue
            elif arr[i+1] < arr[i]:
                return i
        