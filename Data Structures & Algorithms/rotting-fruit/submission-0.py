class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # hashmap where key is (row,col) and val is turns to rot (initialize as -1)
        ROWS,COLS = len(grid),len(grid[0])
        deltas = [[0,1],[-1,0],[0,-1],[1,0]]
        fresh = set()
        visited = set()
        queue = deque()
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    fresh.add((r,c))
                elif grid[r][c] == 2:
                    visited.add((r,c))
                    queue.append((r,c))
        time = 0
        while queue and fresh:
            time += 1
            for i in range(len(queue)):
                r,c = queue.popleft()
                for dr,dc in deltas:
                    newr,newc = r + dr, c + dc
                    if min(newr,newc) < 0 or newr > ROWS - 1 or newc > COLS - 1 or (newr,newc) in visited or grid[newr][newc] == 0:
                        continue
                    fresh.remove((newr,newc))
                    queue.append((newr,newc))
                    visited.add((newr,newc))
        if fresh:
            return -1
        return time
        