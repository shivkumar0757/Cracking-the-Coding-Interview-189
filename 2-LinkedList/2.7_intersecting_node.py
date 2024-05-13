'''
Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the 
intersecting node. Note that the intersection is defined based on reference, not value. That is, if the 
kth node of the first linked list is the exact same node (by reference) as the jth node of the second 
linked list, then they are intersecting.
'''
from linked_list import LinkedList, Node


# approach 1 using the map or set to store the visited nodes
# create a hashmap, start moving among both linkedlist, and check if any one is perent in the set
# if yes, return this node
def find_intersection_memo(ll1, ll2):
    visited = set()
    while ll1 and ll2:
        if ll1 in visited:
            return ll1
        visited.add(ll1)
        if ll2 in visited:
            return ll2
        visited.add(ll2)
        ll1 = ll1.next
        ll2 = ll2.next

    return None


# Approach 2: without memory, by taking length and then starting at diff k, in larger list
# find length of two lists , get diff = k
# for larger list, move the pointer by k
# now start traversing from both lists, untill both of them are not pointing to same.
def find_intersection(ll1, ll2):
    def get_length(head):
        counter = 0
        while head:
            counter += 1
            head = head.next
        return counter
    len1 = get_length(ll1)
    len2 = get_length(ll2)

    k = len1 - len2

    if k < 0:
        for i in range(abs(k)):
            ll2 = ll2.next
    if k > 0:
        for i in range(k):
            ll1 = ll1.next
    
    while ll1 and ll2:
        if ll1 == ll2:
            return ll1
        ll1 = ll1.next
        ll2 = ll2.next
    return None
    

ll1 = LinkedList()
ll1.append(1)
ll1.append(2)
ll1.append(3)
ll1.append(9)
ll1.append(8)
ll1.append(7)
ll1.print()

ll2 = LinkedList()
ll2.append(10)
ll2.head.next = ll1.head.next.next.next
ll2.print()

intersection = find_intersection(ll1.head, ll2.head)
if intersection:
    print(intersection.data)
else:
    print(intersection)