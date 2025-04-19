class HashTable:
    def __init__(self):
        self.Max=10
        self.hash_arr = [None for _ in range(self.Max)]
    def get_hash(self, key):
        hash_val=0
        for char in key:
            hash_val += ord(char)
        return hash_val%10
    def get_order(self, index):
        return [*range(index,self.Max)] + [*range(0, index)]
    def __setitem__(self, key, value):
        added = True
        hash_val = self.get_hash(key)
        if self.hash_arr[hash_val] is None:
            self.hash_arr[hash_val] = (key,value)
        elif self.hash_arr[hash_val] is not None and self.hash_arr[hash_val][0]==key:
            self.hash_arr[hash_val] = (key, value)
        else:
            idx_order = self.get_order(hash_val)
            for i in idx_order:
                added=False
                if self.hash_arr[i] is None:
                    self.hash_arr[i] = (key, value)
                    added = True
                    break
        if not added:
            print(self.hash_arr)
            raise Exception("HashTable is Full")
        print(self.hash_arr)
    def __getitem__(self, key):
        hash_value=self.get_hash(key)
        if self.hash_arr[hash_value][0] == key:
            return self.hash_arr[hash_value][1]
        else:
            idx_order = self.get_order(hash_value)
            for i in idx_order:
                if self.hash_arr[i][0] == key:
                    return self.hash_arr[i][1]
                else:
                    raise Exception("Element not found in the hash table")
    def __delitem__(self, key):
        hash_value = self.get_hash(key)
        if self.hash_arr[hash_value][0] == key:
            self.hash_arr[hash_value] = None
        else:
            idx_order = self.get_order(hash_value)
            for i in idx_order:
                if self.hash_arr[i][0] == key:
                    self.hash_arr[i] = None
                    break
                else:
                    raise Exception("Element not found in the hash table")
        print(self.hash_arr)

hash_table = HashTable()
hash_table['Jan 1'] = 1
hash_table['Jan 12'] = 2
hash_table['Jan 3'] = 3
hash_table['Jan 4'] = 4
hash_table['Jan 5'] = 5
hash_table['Jan 6'] = 6
hash_table['Jan 7'] = 7
hash_table['Jan 8'] = 8
hash_table['Jan 9'] = 9
hash_table['Jan 10'] = 10
del hash_table['Jan 1']
hash_table['Jan 11'] = 21

