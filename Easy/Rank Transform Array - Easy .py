'''https://leetcode.com/problems/rank-transform-of-an-array/description/
Example 1:

Input: arr = [40,10,20,30]
Output: [4,1,2,3]
Explanation: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest.

'''
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        store = {}
        sort_arr = sorted(set(arr))
        for i in range (0, len(sort_arr)):
            store[sort_arr[i]] = i+1
        for i in range(0,len(arr)):
            arr[i] = store[arr[i]]
        return arr
