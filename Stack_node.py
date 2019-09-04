class Node:
    def __init__(self,value=None, pointer=None):
        self.value = value
        self.pointer = pointer
    
class Stack:
    def __init__(self):
        self.head = None
        self.count = 0
    
    def isEmpty(self):
        return not bool(self.head)

    def push(self,value):
        self.head = Node(value,self.head)
        self.count +=1
    
    def pop(self):
        if self.count > 0 and self.head:
            node = self.head
            self.head = node.pointer
            self.count -= 1
            return node.value
        else:
            print('Stack is Empty')
    
    def peek(self):
        if self.count > 0 and self.head:
            return self.head.value
        else:
            print('Stack is Empty')

    def _printList(self):
        node = self.head
        while node:
            print(node.value,end=" ")
            node = node.pointer
        print()

if __name__=='__main__':
    stack = Stack()
    if stack.isEmpty():
        for i in range(5):
            stack.push(i)
    stack._printList()
    print(stack.peek())

