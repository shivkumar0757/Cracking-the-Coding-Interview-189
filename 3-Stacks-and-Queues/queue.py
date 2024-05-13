# Implementting queue in python

#  using the linked list

class QueueNode:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    def add(self, data):
        node = QueueNode(data)
        if self.last != None:
            self.last.next = node
        self.last = node
        if self.first == None:
            self.first = node

    def remove(self):
        if self.first == None:
            print("Queue is empty")
            return None
        
        node = self.first
        self.first = self.first.next
        if not self.first:
            self.last = self.first
        return node.data
    
    def peek(self):
        if self.first == None:
            print("Queue is empty")
            return None
        return self.first.data
    
    def is_empty(self):
        return not self.first
    
    def print(self):
       
        head = self.first
        while head:
            print(head.data, end = " -> ")
            head = head.next

        print("None")



# Queue using the list
# not efficient because of removing first element
# list are efficient for appending
def queue_using_list():
    queue = []
    queue.append(2)
    queue.append(4)
    queue.append(6)
    print(queue)
    queue.pop(0)
    print(queue)



# Queue using dequeue
from collections import deque
def de_queue():
    queue = deque()
    queue.append(2)
    queue.append(4)
    queue.append(6)
    print(queue)
    queue.popleft()
    print(queue)


# Testing queue
queue = Queue()
queue.add(2)
queue.add(4)
queue.add(6)
queue.print()

queue.remove()
queue.print()

print('-------- using list')
queue_using_list()

print('--- using deque')
de_queue()