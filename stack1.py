from collections import deque
class stack:
    def __init__(self):
        self.box = deque()
    def add(self, char):
        self.box.append(char)
        return
    def remove(self):
        self.box.pop()
        return
    def length(self):
        return len(self.box)
    def is_match(self, char):
        match_dict = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        if len(self.box) == 0:
            return False
        if match_dict[char] == self.box[-1]:
            return True
        else:
            return False
    def is_balanced(self, equation):
        self.box.clear()
        for char in equation:
            if char in ['[','(','{']:
                self.add(char)
            elif char in [']',')','}']:
                if self.is_match(char):
                    self.remove()
                else:
                    self.add(char)
        return True if len(self.box) == 0 else False

obj=stack()
print(obj.is_balanced("))((a+b}{"))
print(obj.is_balanced("))"))
print(obj.is_balanced("((a+b))"))
print(obj.is_balanced("({a+b})"))
print(obj.is_balanced("[a+b]*(x+2y)*{gg+kk}"))