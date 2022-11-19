class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    def print_list(self):
        '''prints the linked list'''
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    def append_list(self,value):
        '''adds item to the end of the linked list'''
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    def pop(self):
        '''removes the last item from the linked list'''
        if self.length == 0:
            return None
        else:
            pre = self.head
            temp = self.head
            while temp.next:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
    def prepend_list(self,value):
        '''adds an item to the beginning of the linked list'''
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
    def pop_first(self):
        '''removes the first item from the linked list'''
        if self.length == 0:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
        if self.length == 0:
            self.tail = None
    def get_item(self,index):
        '''returns the item at that index'''
        if index < 0 or index > self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    def set_value(self,index,value):
        '''sets/changes the value at the given index'''
        if index < 0 or index > self.length:
            return None
        else:
            temp = self.get_item(index)
            temp.value = value
    def insert_value(self,index,value):
        '''adds an item to a particular index'''
        new_node = Node(value)
        if self.length == 0 or index < 0 or index > self.length:
            return None
        else:
            if index == 0:
                self.prepend_list(value)
            elif index == self.length:
                self.append_list(value)
            else:
                temp = self.get_item(index-1)
                new_node.next = temp.next
                temp.next = new_node
            self.length +=1
    def remove_item(self,index):
        '''removes an item at a particular index'''
        if index < 0 or index > self.length:
            return None
        else:
            if index == 0:
                self.pop_first()
            elif index == self.length:
                self.pop()
            else:
                temp = self.get_item(index)
                pre = self.get_item(index-1)
                pre.next = temp.next
                temp.next = None
            self.length -= 1 
    def reverse_llist(self):
        '''reverses the complete linked list'''
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after






