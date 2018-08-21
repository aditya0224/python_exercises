# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# we need to check loop edge case and empty edge case
class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow_pointer = head
        fast_pointer = head
        
        if (head == None) :
            return None
        
        while(fast_pointer.next != None):
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next
            
            if(fast_pointer.next == None) :
                break;
            else:
                fast_pointer = fast_pointer.next
            
            # loop in linkedlist
            if (slow_pointer == fast_pointer) :
                return None
            
        return slow_pointer;
                