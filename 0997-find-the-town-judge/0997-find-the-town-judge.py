class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        tracker = [0] * n
        
        for a,b in trust:
            tracker[a-1] -= 1
            tracker[b-1] += 1
            
        for i in range(0,n):
            if tracker[i] ==n-1:
                return i+1
        return -1     
        