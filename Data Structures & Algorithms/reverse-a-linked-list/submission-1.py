# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr: #while curr is not null
            temp = curr.next #store curr.next for temp
            curr.next = prev #curr.next now points at the previous
            prev = curr #prev = curr makes it so prev points to the same thing as the curr.
            curr = temp #move the iteration forward
        return prev