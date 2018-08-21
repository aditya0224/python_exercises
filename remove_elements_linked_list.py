# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if (head == None):
            return None
        
        current = head
        previous = None
        while(current != None):
            if (current.val == val):
                if (previous != None):
                    previous.next = current.next
                    current = current.next
                else:
                    head = current.next
                    current = current.next
                    previous = None
            else:
                previous = current
                current = current.next
        return head
        