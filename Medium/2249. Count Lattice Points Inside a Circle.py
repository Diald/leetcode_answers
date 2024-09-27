'''
https://leetcode.com/problems/count-lattice-points-inside-a-circle/description/
Given a 2D integer array circles where circles[i] = [xi, yi, ri] represents the center (xi, yi) and radius ri of the ith circle drawn on a grid, return the number of lattice points that are present inside at least one circle.

Note:

A lattice point is a point with integer coordinates.
Points that lie on the circumference of a circle are also considered to be inside it.
Input: circles = [[2,2,1]]
Output: 5
Explanation:
The figure above shows the given circle.
The lattice points present inside the circle are (1, 2), (2, 1), (2, 2), (2, 3), and (3, 2) and are shown in green.
Other points such as (1, 1) and (1, 3), which are shown in red, are not considered inside the circle.
Hence, the number of lattice points present inside at least one circle is 5.'''
# the main condition for a point to be lattice point i.e to lie in the circumference of the circle
#x^2 + y^2 = r^2

class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        lattice_points = set()
        for x, y, r in circles:
            for i in range(x - r, x + r + 1):
                for j in range(y - r, y + r + 1):
                    if (i - x) ** 2 + (j - y) ** 2 <= r ** 2:
                        lattice_points.add((i, j))

        return len(lattice_points)
