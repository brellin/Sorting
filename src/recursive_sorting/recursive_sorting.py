test_list = [6, 5, 3, 1, 8, 7, 2, 4, 99, 52, 500004, 588841]

# complete the helpe function below to merge 2 sorted arrays


def merge(arrA, arrB):

    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    print(f'arrA: {arrA}, arrB: {arrB}')

    # could be written i = j = k = 0 to declare all equal
    i = 0
    j = 0
    k = 0

    # loop over all instances of each array until i or j has reached their respective length
    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            merged_arr[k] = arrA[i]
            i += 1
        else:
            merged_arr[k] = arrB[j]
            j += 1
        k += 1

    # if there is anything left in arrA or arrB
    while i < len(arrA):
        merged_arr[k] = arrA[i]
        i += 1
        k += 1

    while j < len(arrB):
        merged_arr[k] = arrB[j]
        j += 1
        k += 1

    print(f'return: {merged_arr}')
    return merged_arr

# implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TODO Find the middle point to divide the array into two halves:
    print(arr)
    mid = len(arr) // 2
    first = arr[:mid]
    second = arr[mid:]
    # TODO Call mergeSort for first half:
    first = merge_sort(first) if len(first) > 1 else first
    # TODO Call mergeSort for second half:
    second = merge_sort(second) if len(second) > 1 else second
    # TODO Merge the two halves sorted in step 2 and 3:
    return merge(first, second)


print(merge_sort(test_list))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TODO

    return arr


def merge_sort_in_place(arr, l, r):
    # TODO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
