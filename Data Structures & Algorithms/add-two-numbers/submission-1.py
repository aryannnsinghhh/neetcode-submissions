# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        temp = dummy
        sum = 0
        while l1 and l2:
            sum = l1.val + l2.val + (sum//10)
            temp.next = ListNode(sum % 10)
            l1 = l1.next
            l2 = l2.next
            temp = temp.next
        while l1:
            sum = l1.val + (sum//10)
            temp.next = ListNode(sum % 10)
            l1 = l1.next
            temp = temp.next
        while l2:
            sum = l2.val + (sum//10)
            temp.next = ListNode(sum % 10)
            l2 = l2.next
            temp = temp.next
        if sum//10:
            temp.next = ListNode(sum // 10)
        return dummy.next