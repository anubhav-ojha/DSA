class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        max_heap = []
        for num in nums:
            if num % 2 == 0:
                num = -num
            
            else:
                num = -num * 2

            heapq.heappush(max_heap, num)

        
        min_dev = float('inf')
        min_val = -max(max_heap)

        while len(nums) == len(max_heap):
            curr = -heapq.heappop(max_heap)
            min_dev = min(min_dev, curr- min_val)
            if curr % 2 == 0:
                min_val = min(min_val, curr//2)
                heapq.heappush(max_heap, -curr//2)
            else:
                break
        
        return min_dev

        