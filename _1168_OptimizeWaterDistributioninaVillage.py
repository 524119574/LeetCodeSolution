# There are n houses in a village. We want to supply water for all the houses by building wells and laying pipes.

# For each house i, we can either build a well inside it directly with cost wells[i], or pipe in water from another well to it. The costs to lay pipes between houses are given by the array pipes, where each pipes[i] = [house1, house2, cost] represents the cost to connect house1 and house2 together using a pipe. Connections are bidirectional.

# Find the minimum total cost to supply water to all houses.

 

# Example 1:



# Input: n = 3, wells = [1,2,2], pipes = [[1,2,1],[2,3,1]]
# Output: 3
# Explanation: 
# The image shows the costs of connecting houses using pipes.
# The best strategy is to build a well in the first house with cost 1 and connect the other houses to it with cost 2 so the total cost is 3.
 

# Constraints:

# 1 <= n <= 10000
# wells.length == n
# 0 <= wells[i] <= 10^5
# 1 <= pipes.length <= 10000
# 1 <= pipes[i][0], pipes[i][1] <= n
# 0 <= pipes[i][2] <= 10^5
# pipes[i][0] != pipes[i][1]

"""
I didn't have any clue on how to do it when I saw the question for the first 
time.

A key realization is to transform the question into a Minimum Spanning Tree
(MST) problem, by considering building a wall as equivalent of connection to
House 0 which has the water. 
"""
class Solution(object):
    def minCostToSupplyWater(self, n, wells, pipes):
        """
        :type n: int
        :type wells: List[int]
        :type pipes: List[List[int]]
        :rtype: int
        """
        parents = [i for i in range(n + 1)] # We have added a new House 0.
        
        def find(target):
            """
            Note that this find implementation uses path compression, if this
            technique wasn't employ the time complexity will gets very large, 
            i.e. linear.
            
            The naive implementation looks like this:
            
            if (target != parents[target]):
                return find(parents[target])
            return target

            The path compression technique basically set the parent of the
            target node to be the ultimate parent instead of the intermediate
            parent, which reduces the time when we want to find its parent
            again in the future.

            A visualized example is the following, coming from Geeks for 
            Geeks: https://www.geeksforgeeks.org/union-find-algorithm-set-2-union-by-rank/

            Let the subset {0, 1, .. 9} be represented as below and find() is 
            called for element 3.
                        9
                    /    |    \  
                    4     5      6
                /     \        /  \
                0        3     7    8
                        /  \
                    1    2  

            When find() is called for 3, we traverse up and find 9 as 
            representative of this subset. With path compression, we also make 
            3 as the child of 9 so that when find() is called next time for 1, 
            2 or 3, the path to root is reduced.

                        9
                    /    /  \    \
                    4    5    6     3 
                /           /  \   /  \
                0           7    8  1   2           
            """
            if (target != parents[target]):
                parents[target] = find(parents[target])
            return parents[target]
    
        def union(group1, group2):
            group1Leader = find(group1)
            group2Leader = find(group2)
            parents[group1Leader] = group2Leader
        
        newPipes = [(0, i + 1, wells[i]) for i in range(len(wells))]
        totalPrice = cnt = 0
        
        for end1, end2, price in sorted(newPipes + pipes, key=lambda p:p[2]):
            if (find(end1) != find(end2)):
                union(end1, end2)
                totalPrice += price
                cnt += 1
            if (cnt == n):
                return totalPrice
