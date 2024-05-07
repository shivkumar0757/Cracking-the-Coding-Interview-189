'''
Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list. 
'''

from linked_list import LinkedList
# find length of ll and then return the kth last
def kth_last_elem(ll, k):
    n = 0
    current = ll.head
    while current:
        n+=1
        current = current.next
    if k > n:
        return None
    target = n - k
    curr_ind = 0
    current = ll.head
    while curr_ind < target:
        current = current.next
        curr_ind += 1

    return current.data

# recursive sol
def kth_last_rec(ll, k):
    if not ll:
        return 0
    index = kth_last_rec(ll.next, k) + 1
    if index == k:
        print(ll.data)
    return index

# single pass kth last
# take two pointer, move first to k
# now move both pointers, until fast pointer is null and retunr slow pointer value
def kth_last_single(ll: LinkedList, k: int):
    slow = ll.head
    fast = ll.head

    counter = 0
    while counter < k and fast:
        counter += 1
        fast = fast.next
    if counter < k:
        return None
    
    while fast:
        fast = fast.next
        slow = slow.next

    return slow.data




ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6)
ll.append(7)
ll.append(8)
ll.append(9)
ll.append(10)
ll.print()
kth_last_rec(ll.head, 3)
print(kth_last_single(ll, 3))
    
