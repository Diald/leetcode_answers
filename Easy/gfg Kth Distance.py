'''https://www.geeksforgeeks.org/problems/kth-distance3757/1
Difficulty: EasyAccuracy: 48.69%Submissions: 15K+Points: 2
Given an unsorted array arr and a number k which is smaller than size of the array. Find if the array contains duplicates within k distance.

Examples:

Input: arr[] = [1, 2, 3, 4, 1, 2, 3, 4] and k = 3
Output: false
Explanation: All duplicates are more than k distance away.
Input: arr[] = [1, 2, 3, 1, 4, 5] and k = 3
Output: true
Explanation: 1 is repeated at distance 3.
Constraints:
1 ≤ arr.size() ≤ 106
1 ≤ k < arr.size()
1 ≤ arr[i] ≤ 105'''

class Solution:
    def checkDuplicatesWithinK(self, arr, k):
        # your code
        seen = set()
        for i in range(len(arr)):
            if(arr[i] in seen):
                return True
            seen.add(arr[i])
            if i >= k:
                seen.remove(arr[i - k])
            
        return False
