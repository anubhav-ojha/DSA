# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nxt = curr = ListNode()
        curr = head
        if head:
            nxt = curr.next
        else:
            return head
            
        
        while nxt:
            if curr.val == nxt.val:
                curr.next = nxt.next
                nxt = nxt.next
            else:
                curr = nxt
                nxt = nxt.next
        return head        
        