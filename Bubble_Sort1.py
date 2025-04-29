def bubble_sort(elements_list_dict, key):
    size = len(elements_list_dict)
    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if elements_list_dict[j][key] >= elements_list_dict[j+1][key]:
                tmp = elements_list_dict[j][key]
                elements_list_dict[j][key] = elements_list_dict[j+1][key]
                elements_list_dict[j+1][key] = tmp
                swapped = True
        if not swapped:
           break

if __name__ == "__main__":
    elements_dict = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]
    bubble_sort(elements_dict, key='name')
    print(elements_dict)