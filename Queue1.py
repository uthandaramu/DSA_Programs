from collections import deque

class Binary:
    def __init__(self):
        self.box = deque()
    def add(self, binary):
        self.box.appendleft(binary)
    def remove(self):
        if len(self.box)!=0:
            self.box.pop()
        else:
            print("Queue is empty")
    def front(self):
        return self.box[-1]
    def print_binary(self, n):
        self.box.clear()
        self.add("1")
        for i in range(n):
            print(self.front())
            self.add(self.front() + "0")
            self.add(self.front() + "1s")
            self.remove()

binary_obj = Binary()
binary_obj.print_binary(100)
