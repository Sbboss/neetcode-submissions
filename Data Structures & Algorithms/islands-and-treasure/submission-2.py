class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        rows, cols = len(grid), len(grid[0])
        
        def dfs(r,c, d):

            if not( 0 <= r < rows) or not(0 <= c < cols) or grid[r][c] == -1:
                return
            
            if d > 0 and grid[r][c] == 0:
                return

            if grid[r][c] < d:
                return
            
            grid[r][c] = d
            
            dfs(r+1, c, d+1)
            dfs(r-1, c, d+1)
            dfs(r, c+1, d+1)
            dfs(r, c-1, d+1)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    dfs(i,j,0)
        
