'''https://www.geeksforgeeks.org/problems/split-singly-linked-list-alternatingly/1
Given a singly linked list's head. Your task is to complete the function alternatingSplitList() that splits the given linked list into two smaller lists. The sublists should be made from alternating elements from the original list.
Note: 

The sublist should be in the order with respect to the original list.
Your have to return an array containing the both sub-linked lists.
Examples:

Input: LinkedList = 0->1->0->1->0->1
Output: 0->0->0 , 1->1->1
Explanation: After forming two sublists of the given list as required, we have two lists as: 0->0->0 and 1->1->1.'''
#User function Template for python3
'''
class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

'''

class Solution:
    def alternatingSplitList(self, head):
        #Your code here
        if not head or not head.next:
            return [head, None]
        a = Node(head.data)
        ahead = a
        b = Node(head.next.data)
        bhead = b
        
        head = head.next.next
        while head and head.next:
            a.next = Node(head.data)
            a = a.next
            b.next = Node(head.next.data)
            b = b.next
            head = head.next.next
            
        if head:
            a.next = Node(head.data)
        else:
            a.next = None
        
        b.next = None
        return [ahead, bhead]
