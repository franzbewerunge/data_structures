class Node: 
    def __init__(self, data=None): 
        self.data = data 
        self.next = None 
        self.prev = None

class Queue: 
    def __init__(self): 
        self.head = None 
        self.tail = None 
        self.count = 0 

    def enqueue(self, data):
    
        item = Node(data, None, None)

        if not self.head:
            self.head = item
            self.tail = self.head
            
        else:
            # Next Item becomes current tail
            item.prev = self.tail 
            # Current Item becomes next of current tail
            self.tail.next = item
            # Current Item becomes new tail
            self.tail = item

        self.count += 1

    def dequeue(self, data):
        
        if self.count == 1:
            self.tail, self.head = None 
            self.count = 0
            
        elif self.count > 1:
            self.head = self.head.next
            self.head.prev = None
            self.count -= 1