# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        cur = head
        new_arr = []
        while cur:
            new_arr.append(cur.val)
            cur = cur.next
        
        front_half = new_arr[:len(new_arr)//2]
        back_half = new_arr[len(new_arr)//2:][::-1]

        cur = head
        i = 0
        while i < len(front_half):
            cur.val = front_half[i]
            cur = cur.next
            cur.val = back_half[i]
            cur = cur.next
            i += 1
        if cur:
            cur.val = back_half[-1]


