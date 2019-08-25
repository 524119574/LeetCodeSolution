# 973. K Closest Points to Origin
# Medium

# 612

# 58

# Favorite

# Share
# We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

# (Here, the distance between two points on a plane is the Euclidean distance.)

# You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

 

# Example 1:

# Input: points = [[1,3],[-2,2]], K = 1
# Output: [[-2,2]]
# Explanation: 
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
# Example 2:

# Input: points = [[3,3],[5,-1],[-2,4]], K = 2
# Output: [[3,3],[-2,4]]
# (The answer [[-2,4],[3,3]] would also be accepted.)

class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        pointObjs = [Point(point[0], point[1]) for point in points]
        pointObjs = sorted(pointObjs, key=lambda point : point.dist)
        return [pointObj.toList() for pointObj in pointObjs[:K]]

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dist = x * x + y * y

    def toList(self):
        return [self.x, self.y]


"""
Note that the above algorithm is not the most concise nor the most efficent.
A more concise solution is the following one-liner:
"""
class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        return sorted(points, key=lambda p : p[0] * p[0] + p[1] * p[1])[:K]

"""
A slightly more efficient solution is the following:
"""
class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        heap = []
        for (x, y) in points:
            """
            A mistake that I have made is writing the loop body as:

            if (len(heap) == K):
                heapq.heappop(heap)
            heapq.heappush(heap, (-(x*x + y*y), x, y))

            The problem this can cause is that if the smallest kth elements are
            already in the heap, the largest among the kth smallest one will get
            pop out, which is not what we wanted.
            """
            heapq.heappush(heap, (-(x*x + y*y), x, y))
            if (len(heap) == K + 1):
                heapq.heappop(heap)
        return [[x, y] for (_, x, y) in heap]

"""
The run time complexity is O(NlgK). And we can also apply optimization when
K is larger than N/2 by not inverting the sign, which is keeping a min heap to
store the first (N-k)th furthest points, and we return `point / heap`, i.e.
all the points that is not (N-k) th furthest, a.k.a the kth closest points.
"""
