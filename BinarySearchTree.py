class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def add_child(self,data):
        if self.data == data:
            return #element already exists

        if data < self.data:
            #adding left side
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)

        if data > self.data:
            #adding right side
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            #searching left side
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            #searching right side
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        #left node
        if self.left:
            elements+=self.left.in_order_traversal()
        #root node
        elements.append(self.data)
        #right node
        if self.right:
            elements+=self.right.in_order_traversal()
        return elements

    def find_min(self):
        ptr = self
        while ptr.left:
            ptr = ptr.left
        return ptr.data

    def find_max(self):
        ptr = self
        while ptr.right:
            ptr = ptr.right
        return ptr.data

    def calculate_sum(self):
        elements = self.in_order_traversal()
        return sum(elements)

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)
        return elements

    def pre_order_traversal(self):
        elements =[]
        elements.append(self.data)
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
        return  elements

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            #Leaf Node
            if self.right is None and self.left is None:
                return None
            #Node with one child node
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            #leaf with two child node
            """min = self.right.find_min() #First Approach
            self.data = min
            self.right = self.right.delete(min)"""
            max = self.left.find_max()     #Second Approach
            self.data = max
            self.left = self.left.delete(max)
        return self



def build_tree(elements):
    print(f"Building tree with these {elements} elements")
    root_node = BinarySearchTree(elements[0])
    for i in range(1, len(elements)):
        root_node.add_child(elements[i])
    return root_node

if __name__ == '__main__':
    countries = ["UK", "USA", "India", "Russia", "South Korea", "France"]
    country_tree = build_tree(countries)
    print("Sorted array: ",country_tree.in_order_traversal())
    print("Is China is in the tree: ", country_tree.search("China"))
    print("Is France is in the tree: ", country_tree.search("France"))

    numbers = [15,12,27,7,14,20,88,23]
    numbers_tree = build_tree(numbers)

    print("Sorted in in-order traversal: ", numbers_tree.in_order_traversal())
    print("Sorted in post-order traversal: ", numbers_tree.post_order_traversal())
    print("Sorted in pre-order traversal: ", numbers_tree.pre_order_traversal())

    del_el = 7
    numbers_tree.delete(del_el)
    print("in-order traversal post deleting {:d} : {}".format(del_el, numbers_tree.in_order_traversal()))

    print("Min value is num tree is ", numbers_tree.find_min())
    print("Max value is num tree is ", numbers_tree.find_max())
    print("Calculated sum of num tree is ", numbers_tree.calculate_sum())