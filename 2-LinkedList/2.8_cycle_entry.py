'''
Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the 
beginning of the loop. 
DEFINITION 
Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so 
as to make a loop in the linked list. 
EXAMPLE 
Input: A -> B -> C -> D -> E -> C [the same C as earlier] 
Output: C 
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    # using set
    def detect_cycle_space(self, head):
        if not head: return head
        dp = set()
        while head:
            if head in dp:
                return head
            dp.add(head)
            head = head.next
        return None

    # WIthout using the hmap
    # use slow and fast pointer, move slow pointer by one, fast by two
    # if found cycle, i.e slow == fast then start from start and slow together,
    # when they are same, we are at enrty to cycle
    def detect_cycle_entry_slow_fast(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if not( fast and fast.next):
            return None
        while slow != head:
            slow = slow.next
            head = head.next
        return head






    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.detect_cycle_entry_slow_fast(head)
        # return self.detect_cycle_space(head)
        