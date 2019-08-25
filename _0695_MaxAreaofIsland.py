# 695. Max Area of Island
# Medium

# 1205

# 63

# Favorite

# Share
# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

# Example 1:

# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
# Example 2:

# [[0,0,0,0,0,0,0,0]]
# Given the above grid, return 0.
# Note: The length of each dimension in the given grid does not exceed 50.

"""
A very similar question as question 1162 As far from land as possible.
"""

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j]):
                    grid[i][j] = 0
                    maxArea = max(maxArea, self.findIsland(i, j, grid))
        return maxArea
    
    def findIsland(self, i, j, grid):
        totalValue = 1
        for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if (0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1):
                grid[x][y] = 0
                totalValue += self.findIsland(x, y, grid)
        return totalValue # to account for the size of itself
                
        