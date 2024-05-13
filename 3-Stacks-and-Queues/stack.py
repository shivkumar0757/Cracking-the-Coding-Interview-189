# Implementing a stack class using the Node.

class StackNode:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


class Stack:

    def __init__(self):
        self.top = None

    def push(self, data):
        node = StackNode(data)
        node.next = self.top
        self.top = node
    
    def pop(self):
        if not self.top:
            print("Stack is empty")
            return None
        node = self.top
        self.top = self.top.next
        return node.data
    
    def peek(self):
        if not self.top:
            print("Stack is empty")
            return None
        
        return self.top.data
    
    def print(self):
        head = self.top
        print('printing stack....')
        if not head:
            print("Stack is empty")
        else:
            while head:
                print(head.data)
                head = head.next
        


def stack_using_list():
    stack = []
    stack.append(2)
    stack.append(4)
    stack.append(6)
    print('Printing list stack')
    for el in stack[::-1]: print(el)
    stack.pop()
    print('Printing list stack')

    for el in stack[::-1]: print(el)

#  using deque
from collections import deque

def stack_using_deque():
    stack = deque()

    stack.append(2)
    stack.append(4)
    stack.append(6)
    print(stack)
    stack.pop()
    print(stack)


    
# Testitng out stack
stack = Stack()
stack.push(2)
stack.push(4)
stack.push(6)
stack.print()
stack.pop()
stack.print()

print("----- Stack using the list")
stack_using_list()

print('Using deque')
stack_using_deque()