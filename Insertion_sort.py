def insertion_sort(elements):
    for ptr in range(1, len(elements)):
        anchor = elements[ptr]
        j = ptr-1
        while j>=0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j = j-1
        elements[j+1] = anchor

if __name__ == "__main__":
    input_arr = [11, 9, 29, 7, 2, 15, 28]
    insertion_sort(input_arr)
    print(input_arr)