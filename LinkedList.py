from itertools import count


class Node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None

    def insert_at_begging(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        llstr = ""
        itr = self.head
        while itr:
            llstr+=str(itr.data)+"-->"
            itr = itr.next
        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, datalist):
        self.head=None
        for data in datalist:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Index out of bound: Invalid Index")
        if index == 0:
            self.head=self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count+=1

    def insert_at(self, data, index):
        if index == 0:
            self.insert_at_begging(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = Node(data, itr.next)
                break
            itr = itr.next
            count += 1

    def insert_after_value(self, data_to_locate, data_to_add_next):
        count=0
        itr = self.head
        while itr:
            if itr.next is None and itr.data==data_to_locate:
                self.insert_at_end(data_to_add_next)
                break
            if itr.data == data_to_locate:
                self.insert_at(data_to_add_next, count+1)
                break
            itr = itr.next
            count += 1

    def remove_by_value(self, data):
        itr = self.head
        count = 0
        flag = 0
        while itr:
            if itr.data == data:
                self.remove_at(count)
                flag =1
                break
            itr = itr.next
            count+=1
        if flag==0:
            print(str(data) + " is not found in the linked list")


if __name__ == "__main__":
    """ll = LinkedList()
    ll.insert_values(['apple', 'banana', 'cherry', 'durian', 'elachi'])
    ll.print()
    print(ll.get_length())
    ll.remove_at(2)
    ll.print()
    ll.insert_at('cherry',2)
    ll.print()
    ll.insert_at_end('ramu')
    ll.print()"""
    #Exercise
    ll = LinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print()
    ll.insert_after_value("mango", "apple")  # insert apple after mango
    ll.print()
    ll.remove_by_value("orange")  # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.print()
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()