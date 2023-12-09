''' 
LINK - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1] 


'''


def BinSearch(arr,key,is_search_left):
    n = len(arr)
    l = 0 
    r = n-1
    idx = -1
    while(l<=r):
        mid = l+(r-l)//2
        if(arr[mid]>key):
            r = mid -1
        elif(arr[mid]<key):
            l = mid +1
        else:
            idx = mid
            if is_search_left:
                r = mid -1 
            else:
                l = mid + 1
    return idx
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [BinSearch(nums,target,True), BinSearch(nums,target,False)]
