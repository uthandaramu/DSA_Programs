def bubble_sort(array_list):
    size = len(array_list)
    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if array_list[j] >= array_list[j+1]:
                tmp = array_list[j]
                array_list[j] = array_list[j+1]
                array_list[j+1] = tmp
                swapped = True
        if not swapped:
            break

if __name__ == "__main__":
    array_list = [23, 12, 34, 52, 3, 24, 11, 7, 1]
    bubble_sort(array_list)
    print(array_list)
