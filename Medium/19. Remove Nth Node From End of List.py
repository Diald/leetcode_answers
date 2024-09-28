''' 19. Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/1404647245/
Given the head of a linked list, remove the nth node from the end of the list and return its head.'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ''' find length of ll, find index of node'''
        curr = head
        length = 0
        while curr:
            length +=1
            curr = curr.next
        if(length == 1):
            return head.next
        if(n>length):
            return head
        main = length - n
        if(main==0):
            return head.next
        curr = head
        prev = None
        for i in range(main):
            prev = curr
            curr = curr.next
        prev.next = curr.next
        return head
