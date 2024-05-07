'''
R�mov� Dups! Write code to remove duplicates from an unsorted linked list. 
FOLLOW UP 
How would you solve this problem if a temporary buffer is not allowed? 
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        node = Node(data)

        if not self.head:
            self.head = node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = node

    
    def print(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end = ' -> ')
            current_node = current_node.next
        print('None')


# iterate through linked list, check if element is in set
# if not add it to set and move forward
def remove_duplicates(ll):
    data_set = set()

    curr_node = ll.head
    prev= None
    
    while curr_node:
        if curr_node.data in data_set:
            prev.next = curr_node.next
        else:
            data_set.add(curr_node.data)
            prev = curr_node
        curr_node = curr_node.next


# no space is allowed
def remove_duplicate_space(ll):
    curr_node = ll.head

    while curr_node:
        runner = curr_node
        while runner.next:
            if runner.next.data == curr_node.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        curr_node = curr_node.next



ll = LinkedList()

ll.add(1)
ll.add(1)
ll.add(2)
ll.add(2)
ll.add(3)
ll.add(3)
ll.print()
remove_duplicate_space(ll)
ll.print()
