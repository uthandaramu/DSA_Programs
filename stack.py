sentence = input("Enter a sentence: ")
from collections import deque
box = deque()
for char in sentence:
    box.append(char)
result = ""
for _ in range(len(box)):
    print(box[-1])
    result+=box.pop()
print(result)