# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, ptr1: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = ptr1
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev  
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = self.reverseList(l1)
        temp2 = self.reverseList(l2)
        
        dummy = curr = ListNode()
        carry = 0
        total = 0
        
        while temp1 or temp2 or carry:
            v1 = temp1.val if temp1 else 0
            v2 = temp2.val if temp2 else 0
            
            total = v1 + v2 + carry
            carry = total // 10
            total = total % 10
            curr.next = ListNode(total)
            
            temp1 = temp1.next if temp1 else None
            temp2 = temp2.next if temp2 else None
            curr = curr.next
            
        temp3 = self.reverseList(dummy.next)
        return temp3

        
    
    
    
    
    
      