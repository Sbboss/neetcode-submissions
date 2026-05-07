class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        stack = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def addCell(r, c, d):
            if (not (0 <= r < rows and 0 <= c < cols) or grid[r][c] == -1 or
                (d > 0 and grid[r][c] == 0) or grid[r][c] <= d):
                return
            grid[r][c] = d
            stack.append((r, c, d))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    stack.append((i, j, 0))

        while stack:
            r, c, d = stack.pop()
            for dr, dc in directions:
                addCell(r + dr, c + dc, d + 1)
