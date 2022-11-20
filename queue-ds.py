class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self,value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def enqueue(self,value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
    
    def dequeue(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            self.first = None
            self.last = None
        else:
            temp = self.first 
            self.first = self.first.next
            temp.next = None
        self.length -= 1
myQueue = Queue(2)
myQueue.enqueue(3)
myQueue.enqueue(21)
myQueue.dequeue()
myQueue.print_queue()
