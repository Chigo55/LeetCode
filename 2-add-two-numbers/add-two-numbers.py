# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = num2 = num3 = 0
        i = j = 0
        while l1 is not None:
            num1 += l1.val * 10 ** i
            l1 = l1.next
            i += 1

        while l2 is not None:
            num2 += l2.val * 10 ** j
            l2 = l2.next
            j += 1

        num3 = num1 + num2
        num3 = list(map(int, str(num3)))
        num3.reverse()
        dummy = ListNode()
        l3 = dummy
        for i in num3:
            dummy.next = ListNode(i)
            dummy = dummy.next

        return l3.next