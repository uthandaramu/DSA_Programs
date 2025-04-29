#Hoare partition
def swap(a, b, arr):
    if a != b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp

def partition_index(elements, start_index, end_index):
    pivot_index = start_index
    pivot = elements[pivot_index]
    while start_index < end_index:
        while start_index < len(elements) and elements[start_index] <= pivot:
            start_index+=1
        while elements[end_index] > pivot:
            end_index-=1
        if start_index <= end_index:
            swap(start_index, end_index, elements)
    swap(pivot_index, end_index, elements)
    return end_index

def Quick_sort(elements, start_index, end_index):
    if start_index < end_index:
        pi = partition_index(elements, start_index, end_index)
        Quick_sort(elements, start_index, pi-1)
        Quick_sort(elements, pi+1, end_index)

if __name__ == "__main__":
    input_array = [11,9,29,7,2,15,28]
    Quick_sort(input_array, 0, len(input_array)-1)
    print(input_array)
