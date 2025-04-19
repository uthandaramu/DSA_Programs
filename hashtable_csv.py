import csv

class HashTable:
    def __init__(self):
        self.max_size = 100
        self.hash_arr = [[] for _ in range(100)]
    def get_hash(self, key):
        asci=0
        for c in key:
            asci += ord(c)
        return asci % 100
    def __setitem__(self, key, value):
        hash_key = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.hash_arr[hash_key]):
            if len(element) == 2 and element[0]==key:
                self.hash_arr[hash_key][idx] = (key,value)
                found = True
        if not found:
            self.hash_arr[hash_key].append((key, value))
    def __getitem__(self, key):
        hash_key = self.get_hash(key)
        for idx, element in enumerate(self.hash_arr[hash_key]):
            if element[0] == key:
                return element[1]
    def print_hash_arr(self):
        for i in self.hash_arr:
            if len(i) != 0:
                print(i)

hash_table = HashTable()
with open('data/nyc_weather.csv', mode="r") as file:
    reader = csv.reader(file)
    for data in reader:
        if data[1].isdigit():
            hash_table[data[0]] = data[1]

print(hash_table['Jan 9'])
print(hash_table['Jan 4'])

