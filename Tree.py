class TreeNode:
    def __init__(self,data):
        self.data = data
        self.child = []
        self.parent = None
    def get_level(self):
        level = 0
        itr = self
        while itr.parent:
            level+=1
            itr=itr.parent
        return level
    def add_child(self, child_node):
        child_node.parent = self
        self.child.append(child_node)
    def print_tree(self):
        spaces = "   " * self.get_level()
        prefix = spaces+"|__" if self.parent else ""
        print(prefix + self.data)
        if self.child:
            for child in self.child:
                child.print_tree()

root_node = TreeNode("Electronics")
Tv_node = TreeNode("Tv")
Tv_node2 = TreeNode("Tv")
Tv_node.add_child(TreeNode("LED"))
Tv_node.add_child(TreeNode("LCD"))
root_node.add_child(Tv_node)
root_node.add_child(Tv_node2)
root_node.print_tree()

