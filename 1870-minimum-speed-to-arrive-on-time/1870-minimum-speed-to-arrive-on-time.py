class Solution:
    def check(self, dist: List[int], hour: float, speed: int) -> bool:
        time = 0.0
        i = 0
        while time <= hour and i < len(dist) - 1:
            time += math.ceil(dist[i] / speed)
            i += 1

        time += dist[-1] / speed
        return time <= hour
    
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if hour < len(dist)-1:
            return -1
        left, right = 1, 10**7
        ans = -1
        
        while left <= right:
            
            mid = left + (right - left)//2
            if self.check(dist, hour, mid):
                ans = mid
                right = mid - 1
            else:
                left = mid +1
        return ans        