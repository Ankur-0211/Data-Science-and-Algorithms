# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        current=head

        if head is None:

            return head

        while current is not None and current.next is not None:
            if current.val==val and current==head:
                head=head.next
                current=head
            # elif current.next is not None:
            elif current.next.val==val:
                current.next=current.next.next
            else:
                current=current.next
        
        if head.val==val:
            head=head.next

        return head

            