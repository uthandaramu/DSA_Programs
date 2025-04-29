def insertion_sort(elements):
    for ptr in range(1, len(elements)):
        print(median(elements[:ptr]))
        anchor = elements[ptr]
        j = ptr - 1
        while j>=0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j = j-1
        elements[j+1] = anchor
    print(median(elements))

def median(elements):
    if len(elements) % 2 == 1:
        return elements[len(elements)//2]
    else:
        return (elements[len(elements)//2] + elements[(len(elements)//2) - 1] ) / 2

if __name__ == "__main__":
    input_arr = [2, 1, 5, 7, 2, 0, 5]
    insertion_sort(input_arr)