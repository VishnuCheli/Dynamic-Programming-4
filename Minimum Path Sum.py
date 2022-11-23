class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        m=len(grid)
        n=len(grid[0])
        
        for j in range(n-2,-1,-1):
            grid[m-1][j] += grid[m-1][j+1]
        
        for i in range(m-2,-1,-1):
            grid[i][n-1] += grid[i+1][n-1]
            
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                grid[i][j] += min(grid[i][j+1],grid[i+1][j])
                
        return grid[0][0]