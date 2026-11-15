class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = set()
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited:
                    count += self.bfs(grid, i, j, visited, islands)
        return count

    def bfs(self, grid, r, c, visited, islands):
        ROWS, COLS = len(grid), len(grid[0])
        if (r == ROWS or c == COLS) or min(r,c) < 0 or (r,c) in visited:
            return 0
        visited.add((r,c))
        if grid[r][c] == "0":
            return 0
        islands.add((r,c))
        self.bfs(grid, r + 1, c, visited, islands)
        self.bfs(grid, r - 1, c, visited, islands)
        self.bfs(grid, r, c + 1, visited, islands)
        self.bfs(grid, r, c - 1, visited, islands)
        return 1