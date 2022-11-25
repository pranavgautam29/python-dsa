class HashTable:
    def __init__(self,size=7):
        self.data_map = [None] * size
    
    def __hash(self,key):
        '''assigns a address to the key'''
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash 
    
    def print_table(self):
        '''prints the hash table'''
        for i, val in enumerate(self.data_map):
            print(i,": ",val)

    def set_item(self,key,value):
        '''sets the item at the address in form of a list'''
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key,value])

    def get_item(self,key):
        '''gets the value of the key which is given as the parameter'''
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    def keys(self):
        '''prints all the keys of the hash table'''
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys

my_hash_table = HashTable(size=10)
my_hash_table.set_item("nails", 200)
my_hash_table.set_item("washers", 70)
my_hash_table.print_table()
print(my_hash_table.keys())
print(my_hash_table.get_item('adas'))