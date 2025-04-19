import re

class HashTable:
    def __init__(self):
        self.Max = 100
        self.hash_arr = [[] for _ in range(self.Max)]
    def get_hash_value(self, key):
        value = 0
        for char in key:
            value+=ord(char)
            return value%100
    def set_item(self, key):
        hash_key = self.get_hash_value(key)
        found=False
        for idx, element in enumerate(self.hash_arr[hash_key]):
            if len(element)>0 and element[0]==key:
                self.hash_arr[hash_key][idx]= (element[0], (element[1]+1))
                found=True
        if not found:
            self.hash_arr[hash_key].append((key, 1))
    def print_hash_arr(self):
        for element in self.hash_arr:
            if len(element)>0:
                print(element)

hash_table = HashTable()
with open('data/poem.txt', mode="r") as f:
    lines = f.read()
    words = re.findall(r'\b\w+\b', lines)

for each_word in words:
    hash_table.set_item(each_word)

hash_table.print_hash_arr()