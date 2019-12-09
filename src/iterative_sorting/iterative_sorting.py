test_list = [6, 5, 3, 1, 8, 7, 2, 4]
# Complete the selection_sort() function below


def selection_sort(arr):
    # loop through n-1 elements
    print('Selection sort:')
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i + 1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j
        # swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
        print(f'\t\t{arr[smallest_index]}, {arr[i]}')
    print(arr)
    return arr


selection_sort(test_list)

#  implement the Bubble Sort function below

test_list = [6, 5, 3, 1, 8, 7, 2, 4]


def bubble_sort(arr):

    print('Bubble sort:')
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            print(f'\t{arr[j]}:')
            print(f'\t\tposition from end: {len(arr) - i - 1}')
            print(f'\t\tIs {arr[j]} greater than {arr[j + 1]}?')
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print(
                    f'\t\tswap {arr[j + 1]} with {arr[j]}\n\t\tarr is now {arr}')
            else:
                print('\t\tNEXT!')

    return arr


bubble_sort(test_list)

# STRETCH: implement the Count Sort function below

test_list = [6, 5, 3, 1, 8, 7, 2, 4]


def count_sort(arr, maximum=-1):

    return arr
