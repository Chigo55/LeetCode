# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        import math
        temp = ListNode()
        answer = temp

        node = head
        values = []

        while node is not None :
            values.append(node.val)
            node = node.next
        print(values)
        
        if len(values) % 2 == 0:
            value = values[math.ceil(len(values)//2):]
        else:
            value = values[math.ceil(len(values)//2):]

        for i in value:
            temp.next = ListNode(i)
            temp = temp.next

        return answer.next        