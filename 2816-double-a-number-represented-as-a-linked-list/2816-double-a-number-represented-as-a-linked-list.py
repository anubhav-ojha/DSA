class Solution:
    def doubleIt(self, head: ListNode) -> ListNode:
        # Reverse the linked list
        reversed_list = self.reverse_list(head)
        # Initialize variables to track carry and previous node
        carry = 0
        current, previous = reversed_list, None

        # Traverse the reversed linked list
        while current:
            # Calculate the new value for the current node
            new_value = current.val * 2 + carry
            # Update the current node's value
            current.val = new_value % 10
            # Update carry for the next iteration
            carry = 1 if new_value > 9 else 0
            # Move to the next node
            previous, current = current, current.next

        # If there's a carry after the loop, add an extra node
        if carry:
            previous.next = ListNode(carry)

        # Reverse the list again to get the original order
        result = self.reverse_list(reversed_list)

        return result

    # Method to reverse the linked list
    def reverse_list(self, node: ListNode) -> ListNode:
        previous, current = None, node

        # Traverse the original linked list
        while current:
            # Store the next node
            next_node = current.next
            # Reverse the link
            current.next = previous
            # Move to the next nodes
            previous, current = current, next_node

        # Previous becomes the new head of the reversed list
        return previous