# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        curr=head
        l=1
        while curr.next!=None:
            curr=curr.next
            l+=1
        if n == l:
            return head.next
        curr=head
        for i in range(l-n-1):
            curr=curr.next
        curr.next=curr.next.next
        return head

        