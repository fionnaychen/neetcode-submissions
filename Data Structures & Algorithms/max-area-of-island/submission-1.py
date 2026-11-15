class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0
        rows, cols = len(grid), len(grid[0])
        islandSize = 0
        visited = set()

        def bfs(r, c):
            q = collections.deque()
            curSize = 0
            q.append((r,c))
            visited.add((r,c))
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            while q:
                r , c = q.pop()
                print(r,c)
                curSize += 1
                for dr, dc in directions:
                    newR, newC = r + dr, c + dc
                    if newR < rows and newC < cols and min(newR, newC) >= 0 and grid[newR][newC] == 1 and (newR, newC) not in visited:
                        visited.add((newR, newC))
                        q.append((newR, newC))
            return curSize

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    islandSize = max(bfs(r,c),islandSize)
                visited.add((r,c))
        return islandSize


