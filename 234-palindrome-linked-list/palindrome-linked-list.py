# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        nhead=None
        tail=None
        curr=head
        while curr!=None:
            new_node=ListNode(curr.val)
            if nhead==None:
                nhead=new_node
                tail=new_node
            else:
                tail.next=new_node
                tail=new_node
            curr=curr.next
        prev=None
        nxt=None
        curr1=nhead
        while curr1!=None:
            nxt=curr1.next
            curr1.next=prev
            prev=curr1
            curr1=nxt
        curr1=prev
        curr=head
        while curr!=None and curr1!=None:
            if curr1.val == curr.val:
                curr=curr.next
                curr1=curr1.next
            else:
                return False
        return True

        