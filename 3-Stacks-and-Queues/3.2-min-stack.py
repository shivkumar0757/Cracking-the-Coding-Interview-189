'''
Stack Min: How would you design a stack which, in addition to push and pop, has a function min 
which returns the minimum element? Push, pop and min should all operate in 0(1) time. 
'''

# we will be using two stacks, one will for all elements, another will store the min element only.
# add all to stakc, add to min stack if 
# min stack is null or element is less then top
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, data):
        self.stack.append(data)
        if not self.min_stack or self.min_stack[-1] >= data:
            self.min_stack.append(data)
    
    def pop(self):
        if not self.stack:
            print("Stack is empty")
        else:
            top = self.stack.pop()
            if top == self.min_stack[-1]:
                self.min_stack.pop()
            return top
        
    def get_min(self):
        if not self.min_stack: 
            print("Stack is empty")
            return None
        return self.min_stack[-1]
    
    def print(self):
        if not self.stack:
            print("Stack is empty")
        else:
            print(self.stack[::-1])
            print('min: ', self.min_stack[::-1])



min_stack = MinStack()
min_stack.push(1)
min_stack.push(3)
min_stack.push(5)
min_stack.print()
print(min_stack.get_min())