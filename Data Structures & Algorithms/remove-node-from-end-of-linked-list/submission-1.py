# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reversal(self, head):
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        reversed_head = self.reversal(head)
        t = reversed_head
        if n == 1:
            reversed_head = reversed_head.next
        for i in range(1,n+1):
            if i == n-1:
                t.next = t.next.next
                break
            t = t.next
        return self.reversal(reversed_head)
             