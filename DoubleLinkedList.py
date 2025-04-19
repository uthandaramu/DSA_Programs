class Node():
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DoubleLinkedList():
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        if self.head is None:
            node = Node(data,None, self.head)
            self.head=node
        else:
            node = Node(data, prev=None, next=self.head)
            self.head.prev=node
            self.head=node

    def print_forward(self):
        llstr = ""
        itr = self.head
        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next
        print(llstr)

    def get_last_itr(self):
        itr = self.head
        while itr.next:
            itr=itr.next
        return itr

    def print_backward(self):
        llstr = ""
        itr = self.get_last_itr()
        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.prev
        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data, None, None)
            self.head=node
        else:
            itr=self.head
            itr = self.get_last_itr()
            node = Node(data, itr, None)
            itr.next=node

    def insert_values(self, data_list):
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        length = 0
        itr = self.head
        while itr:
            itr=itr.next
            length+=1
        return length

    def remove_at(self, index):
        if index == 0:
            self.head = self.head.next
            self.head.prev=None
            return
        count = 0
        itr = self.head
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                return
            itr = itr.next
            count+=1

    def insert_at(self,data, index):
        if index == 0:
            node = Node(data, None, self.head)
            self.head.prev=node
            self.head=node
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                node = Node(data, itr, itr.next)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break
            count+=1
            itr=itr.next

if __name__=='__main__':
    dll = DoubleLinkedList()
    dll.insert_values(["apple","ball", "cat", "dog", "elephant"])
    dll.print_forward()
    dll.print_backward()
    dll.insert_at("xavier",2)
    dll.print_forward()
    dll.print_backward()
