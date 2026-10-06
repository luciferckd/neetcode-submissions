from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        island = 0

        def bfs(r, c):
            queue = deque([(r, c)])
            visit.add((r, c))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            while queue:
                row, col = queue.popleft()

                for dr, dc in directions:
                    r, c = row + dr, col + dc

                    if (0 <= r < rows and 0 <= c < cols and grid[r][c] == "1" and (r, c) not in visit):
                        queue.append((r, c))
                        visit.add((r, c))



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    island += 1
        return island