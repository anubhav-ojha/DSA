from typing import List
from queue import Queue

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        n = len(grid)
        dx = [-1, 0, 1]
        dy = [-1, 0, 1]
        
        queue = Queue()
        queue.put([0, 0, 1])
        grid[0][0] = 1
        
        while not queue.empty():
            x, y, steps = queue.get()
            
            if x == n - 1 and y == n - 1:
                return steps
            
            for i in range(3):
                for j in range(3):
                    nx = x + dx[i]
                    ny = y + dy[j]
                    
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                        queue.put([nx, ny, steps + 1])
                        grid[nx][ny] = 1
        
        return -1