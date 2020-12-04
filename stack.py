class Node: 
    def __init__(self, data=None): 
        self.data = data 
        self.next = None 

class Stack: 
    def __init__(self): 

        self.top = None 
        self.size = 0

    def push(self, data):

        node = Node(data)

        if not self.top:
            self.top = node
        
        else:
            # make previous top element to next of new top
            node.next = self.top
            self.top = node
        
        self.size += 1
    
    def pop(self):

        if self.top:
            # remove current top from stack and return
            current_item = self.top
            self.top  = self.top.next
            self.size -= 1
            return current_item.data

        return None

    def peek(self):
        if self.top:
            return self.top.data

        return None

