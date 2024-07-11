# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next #beginning of second half

        prev, slow.next = None, None
        
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp 
            #exact same logic as reversing normal LL

        #now we need to merge 

        first, second = head, prev #prev is now the beginning of the second half list which all points the other way
        #so now we have the starts of both lists

        while second:
            #1234 becomes 1423
            tmp1, tmp2 = first.next, second.next

            first.next = second 
            second.next = tmp1

            first = tmp1
            second = tmp2


        




        