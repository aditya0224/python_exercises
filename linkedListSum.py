# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry_on = 0		
        head = ListNode(None)
        previousNode = None
        while (l1 is not None or l2 is not None) or (carry_on > 0):
            
            value = 0
            if l1 is not None:
                value += l1.val
            
            if l2 is not None:
                value += l2.val
            
            value += carry_on
            
            resultNode = ListNode(None)
            if value >= 10:
                carry_on = value // 10
                resultNode.val = value % 10
            else:
                carry_on = 0
                resultNode.val = value
                
            if previousNode is None:
                previousNode = resultNode
                head = resultNode
            else:
                previousNode.next = resultNode
            
            previousNode = resultNode
            if l1 is not None:     
                l1 = l1.next
            if l2 is not None:            
                l2 = l2.next
                
        return head