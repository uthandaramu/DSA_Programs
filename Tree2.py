class TreeNode:
    def __init__(self,data):
        self.data = data
        self.child = []
        self.parent = None
    def get_level(self):
        level = 0
        ptr = self
        while ptr.parent:
            level+=1
            ptr = ptr.parent
        return level
    def add_child(self, child_node):
        child_node.parent = self
        self.child.append(child_node)
    def print_tree(self, level):
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.child and level>0:
            for element in self.child:
                element.print_tree(level-1)

def build_location_tree():
    root_node = TreeNode("Global")
    country_node1 = TreeNode("India")
    country_node2 = TreeNode("USA")
    state_node1 = TreeNode("Gujarat")
    state_node2 = TreeNode("Karnataka")
    state_node3 = TreeNode("New Jersey")
    state_node4 = TreeNode("California")
    root_node.add_child(country_node1)
    root_node.add_child(country_node2)
    country_node1.add_child(state_node1)
    country_node1.add_child(state_node2)
    country_node2.add_child(state_node3)
    country_node2.add_child(state_node4)
    state_node1.add_child(TreeNode("Ahmedabad"))
    state_node1.add_child(TreeNode("Baroda"))
    state_node2.add_child(TreeNode("Bangalore"))
    state_node2.add_child(TreeNode("Mysore"))
    state_node3.add_child(TreeNode("Princeton"))
    state_node3.add_child(TreeNode("Trenton"))
    state_node4.add_child(TreeNode("San Francisco"))
    state_node4.add_child(TreeNode("Mountain View"))
    state_node4.add_child(TreeNode("Palo Alto"))
    return root_node

if __name__ == '__main__':
    root_node = build_location_tree()
    root_node.print_tree(3)
