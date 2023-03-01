class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) // 2, -1, -1):
            self.max_heapify(nums, i, len(nums))
        
        # sort the array using heapsort
        for i in range(len(nums) - 1, 0, -1):
            # swap the root node with the last node in the heap
            nums[0], nums[i] = nums[i], nums[0]
            # maintain the max heap property on the remaining heap
            self.max_heapify(nums, 0, i)
        
        return nums
    
    def max_heapify(self, nums, i, n):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i
        if left < n and nums[left] > nums[largest]:
            largest = left
        if right < n and nums[right] > nums[largest]:
            largest = right
        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]
            self.max_heapify(nums, largest, n)
        