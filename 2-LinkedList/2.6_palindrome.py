'''
2.6 Palindrome: Implement a function to check if a linked list is a palindrome. 
'''
from linked_list import LinkedList, Node

def add_before(ll, val):
    return Node(val, ll)
    
# using new list to check if it is a palindrome
def is_palindrome_new_list(ll):
    head = None
    temp = ll
    while ll:
        node = Node(ll.data, head)
        head = node
        ll = ll.next
    ll = temp

    while ll and head:
        if ll.data != head.data:
            return False
        ll = ll.next
        head = head.next
    return True

# single iteration using stack
# use slow and fast pointer, add slow pointer data to stack
#  and handle even and odd length(if slow != null, slow = slow.next), 
# compare stack top and pop form stack and move slow pointer
def is_palindrome_stack(head):
    slow = head
    fast = head
    stack = []

    while fast and fast.next:
        stack.append(slow.data)
        slow = slow.next
        fast = fast.next.next
    
    if fast:
        slow = slow.next   # if fast is not None, i.e. odd length and move slow by on

    while slow:
        top = stack.pop()
        if top != slow.data:
            return False
        slow = slow.next
    return True



# approach 3 reversing the second half of linked list.

# find teh middle point, using slow and fast pointer
# if fast is not None, i.e. odd length, now move slow to next of slow
# now rev this list and compare two lists, and compare till rev list is not None
def rev_list(head):
    prev = None
    curr= head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

        
def is_palindrome_rev(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next

    if fast:
        slow = slow.next
    rev = rev_list(slow)
    first_half = head
    while rev:
        if rev.data != first_half.data:
            return False
        rev = rev.next
        first_half = first_half.next
    return True


# using slow pointer and recursion
# find the length, and if length is 0 or one if len is 0 i.e even else odd
# if len == 0 start returning head, else return head.next , true or false
class NodeBool:
    def __init__(self, node = None, is_palindrome = False):
        self.node = node
        self.is_palindrome = is_palindrome


def is_palindrome_rec(ll):
    def get_length(head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length
    def helper(head, length):
        if not head or length <= 0:
            return NodeBool(head, True)
        if length == 1:
            return NodeBool(head.next, True)
        
        res = helper(head.next, length - 2)
        node = res.node
        is_palindrome = res.is_palindrome and (head.data == res.node.data)
        return NodeBool(node.next, is_palindrome)
    
    length = get_length(ll)
    return helper(ll, length).is_palindrome



    
ll = LinkedList()
ll.append(1)
ll.append(2)
# ll.append(2)
ll.append(2)
ll.append(1)


ll.print()
print(f"using new list, is palindrome?: {is_palindrome_new_list(ll.head)}")
print(f"using stack, is palindrome?: {is_palindrome_stack(ll.head)}")
print(f"using recursion, is palindrome?: {is_palindrome_rec(ll.head)}")
print(f"using in place modification , is palindrome?: {is_palindrome_rev(ll.head)}")




