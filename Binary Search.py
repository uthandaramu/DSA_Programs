class BinarySearch:
    def __init__(self, num_array):
        self.num_array = num_array

    def binary_search(self, num_to_find, left_index, right_index, mid_index = 0):
        while left_index <= right_index:
            mid_index = (left_index + right_index) // 2
            mid_val = self.num_array[mid_index]
            if mid_val == num_to_find:
                return mid_index
            if mid_val < num_to_find:
                left_index = mid_index + 1
            else:
                right_index = mid_index - 1
        return -1

    def binary_search_recursion(self, num_to_find, left_index, right_index):
        if left_index > right_index:
            return -1
        mid_index = (left_index + right_index) // 2
        if mid_index >= len(self.num_array) or mid_index < 0:
            return -1
        mid_val = self.num_array[mid_index]
        if mid_val == num_to_find:
            return mid_index
        if num_to_find < mid_val:
            right_index = mid_index-1
        else:
            left_index = mid_index + 1
        return self.binary_search_recursion(num_to_find, left_index, right_index)

    def find_all_occurence(self, num_to_find, start_index, end_index):
        index = self.binary_search(num_to_find, start_index, end_index)
        index_array = []
        i = index
        while i >= 0:
            if self.num_array[i] == num_to_find:
                index_array.append(i)
                i -= 1
                if i == -1:
                    break
            else:
                break
        i = index+1
        while i <= len(self.num_array)-1:
            if self.num_array[i] == num_to_find:
                index_array.append(i)
                i += 1
            else:
                break
        return index_array


if __name__ == "__main__":
    array = [1,4,6,9,11,15,15,15]
    find_obj = BinarySearch(array)
    #index = find_obj.find_all_occurence(15, 0, len(array)-1)
    index_rec = find_obj.find_all_occurence(15, 0, len(array)-1)
    print(f"Element found at {index_rec} position")
    #print(f"Element found at {index_rec} position")

