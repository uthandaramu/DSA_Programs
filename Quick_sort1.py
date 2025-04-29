#Lomuto Partition
def swap(a, b, arr):
    arr[a], arr[b] = arr[b], arr[a]

def partition_index(elements, start_index, end_index):
    pivot_index = end_index
    pivot = elements[pivot_index]
    p_index = start_index

    for i in range(start_index, end_index):
        if elements[i] <= pivot:
            swap(p_index, i, elements)
            p_index += 1
    swap(p_index, end_index, elements)
    return p_index

def quick_sort(elements, start_index, end_index):
    if start_index < end_index:
        pi = partition_index(elements, start_index, end_index)
        quick_sort(elements, start_index, pi-1)
        quick_sort(elements, pi+1, end_index)

if __name__ == "__main__":
    input_array = [2,1]
    quick_sort(input_array, 0, len(input_array)-1)
    print(input_array)