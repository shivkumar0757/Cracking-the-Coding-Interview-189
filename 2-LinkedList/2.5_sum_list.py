'''
Sum Lists: You have two numbers represented by a linked list, where each node contains a single 
digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a 
function that adds the two numbers and returns the sum as a linked list. 
EXAMPLE 
Input: (7-> 1 -> 6) + (5 -> 9 -> 2).Thatis,617 + 295. 
Output: 2 -> 1 -> 9. That is, 912. 
FOLLOW UP 
Suppose the digits are stored in forward order. Repeat the above problem. 
EXAMPLE 
lnput:(6 -> 1 -> 7) + (2 -> 9 -> 5).Thatis,617 + 295. 
Output: 9 -> 1 -> 2. That is, 912.
'''

from linked_list import LinkedList, Node

def sum_lists_rev(ll1, ll2):
    
    carry = 0
    prev = None
    while ll1 and ll2:
        digit_sum = ll1.data + ll2.data + carry
        carry = digit_sum // 10
        ll1.data = digit_sum % 10
        prev = ll1
        ll1 = ll1.next
        ll2 = ll2.next
    # print(prev.data)
    if ll2:
        prev.next = ll2
   

    ll1 = prev.next
    if ll1:
        curr_sum = ll1.data + carry
        carry = curr_sum // 10
        ll1.data = curr_sum % 10
        prev = ll1
        ll1 = ll1.next

    if carry > 0:
        node = Node(carry)
        prev.next = node


class SumNode:
    def __init__(self,node, carry):
        self.node = node
        self.carry = carry


def sum_list(ll1, ll2):
    def length(ll1):
        length = 0
        while ll1:
            length+=1
            ll1 = ll1.next
        return length
    
    def add_padding(ll, n):
        for i in range(n):
            ll = add_before(ll, 0)
        return ll
    
    def add_before(ll, val):
        node = Node(val)
        node.next = ll
        return node
    
    
    def helper(ll1, ll2):
        if (not ll1 and not ll2):
            return SumNode(None, 0)
        
        res = helper(ll1.next, ll2.next)

        curr_sum = ll1.data + ll2.data + res.carry

        node = add_before(res.node, curr_sum % 10)
        return SumNode(node, curr_sum // 10) # return new node and carry as tuple of size 2
    

    len1 = length(ll1)
    len2 = length(ll2)

    padding = len1 - len2

    if padding < 0:
        ll1 = add_padding(ll1, abs(padding))
    if padding > 0:
        ll2 = add_padding(ll2, padding)
    res = helper(ll1, ll2)

    if res.carry > 0:
        return add_before(res.node, res.carry)
    else:
        return res.node

    


    
        


        


ll1 = LinkedList()
ll1.append(1)
ll1.append(2)
ll1.append(1)
ll1.print()

ll2 = LinkedList()
ll2.append(9)
ll2.append(9)
ll2.append(8)
ll2.print()

sum_lists_rev(ll1.head, ll2.head)
ll1.print()

print('----- non rev sum')
ll1 = LinkedList()
ll1.append(1)
ll1.append(1)
ll1.append(1)
ll1.print()

ll2 = LinkedList()
ll2.append(9)
ll2.append(2)
ll2.append(2)
ll2.print()

res = LinkedList()
res.head = sum_list(ll1.head, ll2.head)
res.print()

