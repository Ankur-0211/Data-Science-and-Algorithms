# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        current=head
        temp=current
        count=0

        if head:

            while temp is not None:
                count+=1
                temp=temp.next
            print(count)
            
            pos=(count-n)-1

            while pos>0:
                current=current.next
                pos-=1
            print(pos)
            print(current.val)

            if pos<0:
                head=head.next
            
            if current.next !=None:
            
                current.next=current.next.next
        else:
            head=None

        return head

        