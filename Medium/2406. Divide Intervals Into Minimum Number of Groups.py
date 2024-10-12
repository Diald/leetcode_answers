''' https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/description/
You are given a 2D integer array intervals where intervals[i] = [lefti, righti] represents the inclusive interval [lefti, righti].

You have to divide the intervals into one or more groups such that each interval is in exactly one group, and no two intervals that are in the same group intersect each other.

Return the minimum number of groups you need to make.

Two intervals intersect if there is at least one common number between them. For example, the intervals [1, 5] and [5, 8] intersect.

 

Example 1:

Input: intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]
Output: 3
Explanation: We can divide the intervals into the following groups:
- Group 1: [1, 5], [6, 8].
- Group 2: [2, 3], [5, 10].
- Group 3: [1, 10].
It can be proven that it is not possible to divide the intervals into fewer than 3 groups.
'''

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        start_points = sorted(i[0] for i in intervals)
        ending_points = sorted(i[1] for i in intervals)

        count = 0
        e = 0
        
        for start in start_points: 
            if(start>ending_points[e]):
                e +=1
            else:
                count+=1
        
        return count

''' we make 2 arrays having the starting points and ending points and we sort it and if the start point is greater than end point it will not be considered'''
