# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        # lets explain using NULL -> 0 -> 1 -> 2 -> NULL

        while curr:
            tmp = curr.next #tmp = 1
            curr.next = prev #0 arrow points to NONE now ie has been reversed
            prev = curr #time to move ahead so curr pointer is on 0 now from NULL
            curr = tmp #current is on 1 now since tmp was 1
        return prev

        