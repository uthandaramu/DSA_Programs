class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
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
        child_node.parent=self
        self.child.append(child_node)
    def print_tree(self, type):
        value = ""
        match (type.lower()):
            case "name":
                value+=self.name
            case "designation":
                value+=self.designation
            case "both":
                value+=self.name + " (" + self.designation + ")"
            case _:
                print("Invalid Option")
                return
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix+value)
        if self.child:
            for i in self.child:
                i.print_tree(type)


def build_management_tree():
    root_node = TreeNode("Nilupul","CEO")
    first_level_1 = TreeNode("Chinmay","CTO")
    first_level_2 = TreeNode("Gels","HR Lead")
    second_level_1 = TreeNode("Vishwa","Infrastructure Head")
    second_level_2 = TreeNode("Aamir","Application Head")
    second_level_3 = TreeNode("Peter","Recruitment Manager")
    second_level_4 = TreeNode("Waqas","Policy Manager")
    second_level_1.add_child(TreeNode("Dhaval","Cloud Manager"))
    second_level_1.add_child(TreeNode("Abhijit", "App Manager"))
    first_level_1.add_child(second_level_1)
    first_level_1.add_child(second_level_2)
    first_level_2.add_child(second_level_3)
    first_level_2.add_child(second_level_4)
    root_node.add_child(first_level_1)
    root_node.add_child(first_level_2)
    return root_node


if __name__ == '__main__':
    root_node = build_management_tree()
    root_node.print_tree("name") # prints only name hierarchy
    root_node.print_tree("designation") # prints only designation hierarchy
    root_node.print_tree("both") # prints both (name and designation) hierarchy"""