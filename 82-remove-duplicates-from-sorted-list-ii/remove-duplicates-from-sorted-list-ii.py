# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        new_head=None
        tail=None
        curr=head
        while curr!=None:
            if curr.next!=None and curr.val==curr.next.val:
                duplicate=curr.val
                while curr!=None and curr.val==duplicate:
                    curr=curr.next
            else:
                new_node = ListNode(curr.val)
                if new_head==None:
                    new_head=new_node
                    tail=new_node
                else:
                    tail.next = new_node
                    tail = new_node
                curr = curr.next
        return new_head