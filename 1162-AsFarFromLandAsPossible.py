# Given an N x N grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized and return the distance.

# The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

# If no land or water exists in the grid, return -1.

 

# Example 1:



# Input: [[1,0,1],[0,0,0],[1,0,1]]
# Output: 2
# Explanation: 
# The cell (1, 1) is as far as possible from all the land with distance 2.
# Example 2:



# Input: [[1,0,0],[0,0,0],[0,0,0]]
# Output: 4
# Explanation: 
# The cell (2, 2) is as far as possible from all the land with distance 4.

"""
This is a question that I couldn't solve during the contest. So, do revisit similar question. A similar question might be
#200 Number of Islands.
"""
# Below is the solution that I came up during the contest. I am sure this solution is correct, how it takes too long to execute.
class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        lands = set()
        waters = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j] == 1):
                    lands.add((i, j))
                else:
                    waters.add((i, j))
        if (len(lands) == 0 or len(waters) == 0):
            return -1
        
        maxdist = -10e9
        for water in waters:
            dist = self.findClosestLand(water[0], water[1], lands)
            if (maxdist < dist):
                maxdist = dist
        return maxdist
        
    def findClosestLand(self, i, j, lands):
        mindist = 10e9
        for land in lands:
            dist = self.distance(i, j, land)
            if (mindist > dist):
                mindist = dist
        return mindist
            
    
    def distance(self, i, j, land):
        return abs(i - land[0]) + abs(j - land[1])

"""
During the contest I had a vague idea of doing a depth first search. Namely by keeping a counter starting with 1. Each time we start from the land
and then go out to hunt for the water. We increment the counter by 1 during each iteration. 
This process terminates once all of the area has been reached. We then return the counter name. However, I wasn't able to code up a solution. 
Mainly due to the fact that I am not sure if this land has been visited or not. 
"""
# The key is to keep a list of the *edge* land. And we only store the land that is recently added, and also we change the original grid.
class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        height = len(grid)
        width = len(grid[0])
        
        edgeLands = list()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j] == 1):
                    edgeLands.append((i, j))
        
        if (len(edgeLands) == 0 or len(edgeLands) == width * height):
            return -1
        
        level = 0
        while (edgeLands):
            oldSize = len(edgeLands)
            for i in range(oldSize):
                corners = [(1, 0), (-1, 0), (0, 1), (0,-1)]
                x, y = edgeLands.pop(0)
                for corner in corners:
                    xi = x + corner[0]
                    yi = y + corner[1]
                    if (xi >= 0 and xi < height and yi >= 0 and yi < width and grid[xi][yi] == 0):
                        grid[xi][yi] = 1
                        edgeLands.append((xi, yi))
            level += 1
        return level - 1        