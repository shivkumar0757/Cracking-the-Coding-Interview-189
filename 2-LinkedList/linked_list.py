
class Node:
    def __init__(self, data = 0, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data)

        if not self.head:
            self.head = node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = node

    def delete_node(self, data):
        # find the node, keep track of previous, do prev.next = current.next
        if not self.head:
            print('list is empty')
            return
        n = self.head
        if n.data == data:
            return n.next
        
        while n.next:
            if n.next.data == data:
                n.next = n.next.next
                return self.head
            n = n.next

        

    def print(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end = ' -> ')
            current_node = current_node.next
        print('None')


# ll = LinkedList()
# ll.append(1)
# ll.print()
# ll.append(2)
# ll.append(3)
# ll.append(4)
# ll.print()
# ll.delete_node(3)
# ll.print()