''' Example 1:

Input: arr1 = [1,10,100], arr2 = [1000]
Output: 3
Explanation: There are 3 pairs (arr1[i], arr2[j]):
- The longest common prefix of (1, 1000) is 1.
- The longest common prefix of (10, 1000) is 10.
- The longest common prefix of (100, 1000) is 100.
The longest common prefix is 100 with a length of 3.
Example 2:

Input: arr1 = [1,2,3], arr2 = [4,4,4]
Output: 0
Explanation: There exists no common prefix for any pair (arr1[i], arr2[j]), hence we return 0.
Note that common prefixes between elements of the same array do not count.'''
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefix_map = {}
        for num in arr1:
            curr = str(num)
            prefix = ""
            for ch in curr:
                prefix+=ch
                prefix_map[prefix] = prefix_map.get(prefix,0)+1 #get will get the value where key is prefix otherwise its 0
        max_len = 0
        for num in arr2:
            curr = str(num)
            prefix = ""
            for ch in curr:
                prefix+=ch
                if prefix in prefix_map.keys():
                    max_len = max(max_len,len(prefix))
        return max_len
