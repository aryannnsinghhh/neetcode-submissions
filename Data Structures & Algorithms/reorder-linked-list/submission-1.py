# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # 3 stages: finding middle split, reverse second half, start merging nodes one by one
        # finding middle split:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        curr = slow.next
        slow.next = None # splitting

        # reversing second half
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # start merging
        first, second = head, prev
        while first and second:
            temp1, temp2 = first.next, second.next
            first.next = second
            first = temp1
            second.next = first
            second = temp2