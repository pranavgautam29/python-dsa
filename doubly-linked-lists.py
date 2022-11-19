class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        '''prints the doubly linked list'''
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append_dll(self, value):
        '''adds an item to the end of the doubly linked list'''
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        '''removes the last element from the doubly linked list'''
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1

    def prepend_dll(self, value):
        '''adds and item to the start of the doubly linked list'''
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def pop_first(self):
        '''removes the item at the starting of the doubly linked list'''
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.head.prev = None
        self.length -= 1

    def get_item(self, index):
        if index < 0 or index >= self.length:
            return None
        else:

            if index < self.length/2:
                temp = self.head
                for _ in range(index):
                    temp.next
            else:
                temp = self.tail
                for _ in range(self.length-1, index, -1):
                    temp.prev
        return temp

    def set_item(self, index, value):

        temp = self.get_item(index)
        if temp:
            temp.value = value
        else:
            return False

    def insert_item(self,index,value):
        new_node = Node(value)
        if index < 0 or index >= self.length:
            return None
        else:
            if index == 0:
                self.prepend_dll(value)
            elif index == self.length:
                self.append_dll(value)
            else:
                pre = self.get_item(index-1)
                temp = pre.next
                new_node.prev = pre
                new_node.next = temp
                pre.next = new_node
                temp.prev = new_node
        self.length += 1
        return True


