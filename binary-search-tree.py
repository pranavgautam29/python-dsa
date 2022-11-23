class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None 

    def insert_value(self,value):
        '''inserts a new node in a binary search tree at the appropriate position'''
        new_node = Node(value)
        if self.root is None :
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self,value):
        '''checks if a value is present in a binary search tree or not'''
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    def min_value_node(self,current_node):
        '''gives the minimum value node'''
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value
        


my_tree = BinarySearchTree()
my_tree.insert_value(2)
my_tree.insert_value(10)
my_tree.insert_value(3)
print(my_tree.min_value_node(my_tree.root))
        