'''
 Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but 
the first and last node, not necessarily the exact middle) of a singly linked list, given only access to 
that node. 
EXAMPLE 
lnput:the node c from the linked lista->b->c->d->e->f 
'''
# implemented at bottom of this code. before testing.

from linked_list import LinkedList, Node

#  we can count n and then delete n//2 th node, but we will not implement it

# use slow and fast pointer, for each step, move slow by one and fast by 2

def del_middle(ll):
    tempNode = Node(0)
    tempNode.next = ll.head
    slow = tempNode
    fast = tempNode
    slow_prev = None

    while fast and fast.next:
        slow_prev = slow
        slow = slow.next
        fast = fast.next.next
    slow_prev.next = slow_prev.next.next


# Problem mentioned in the book
def delete_node(node):
    if node is None or node.next is None:
        return False  # Failure, as we cannot delete the last node using this method.
    next_node = node.next
    node.data = next_node.data
    node.next = next_node.next
    return True  # Successful deletion.

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
del_middle(ll)
ll.print()

# Create the linked list and append elements
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)

# Print original list
print("Original List(book test case):")
ll.print()

# Assuming we want to delete the node containing '3'
node_to_delete = ll.head.next.next  # This points to the node containing '3'

# Delete the node and check if it was successful
if delete_node(node_to_delete):
    print("Node deleted successfully.")
else:
    print("Failed to delete node.")

# Print modified list
print("Modified List:")
ll.print()
