''' Maximum Product Subarray
Difficulty: MediumAccuracy: 18.09%Submissions: 390K+Points: 4
Given an array arr[] that contains positive and negative integers (may contain 0 as well). Find the maximum product that we can get in a subarray of arr.

Note: It is guaranteed that the output fits in a 32-bit integer.

Examples

Input: arr[] = [-2, 6, -3, -10, 0, 2]
Output: 180
Explanation: The subarray with maximum product is {6, -3, -10} with product = 6 * (-3) * (-10) = 180.'''

def Solution(arr):
  n = len(arr)
  curr_max = arr[0]
  curr_min = arr[0]
  global_max = arr[0]
  for i in range(1,n):
    num = arr[i]
    if(num<0):
      curr_min, curr_max = curr_max, curr_min
    curr_max = max(num, curr_max*num)
    curr_min = min(num, curr_min*num)
    global_max = max(global_max, curr_max)
  return global_max
      
