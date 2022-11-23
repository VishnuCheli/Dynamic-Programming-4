#Try method with less space
#         prevrow = [1] *n

#         if m ==1:
#             return 1

#         for i in range(m-1):
#             currRow = [1]*n
#             for j in range(n-2,-1,-1):
#                 currRow[j] = currRow[j+1] + prevrow[j]

#             prevrow = currRow

#         return currRow[0]
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m==1:
            return 1
        
        grid = [[1 for j in range(n)] for i in range(m)]
        
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                grid[i][j] = grid[i][j+1] + grid[i+1][j]
        return(grid[0][0])