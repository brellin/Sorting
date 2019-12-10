test_array = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]

# STRETCH: implement Linear Search


def linear_search(arr, target):

    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1


# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):

    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr) - 1

    while low <= high:

        # calculate the middle of the array
        middle = (low + high) // 2

        # if middle is target, return it
        if arr[middle] == target:
            return middle

        # if target is less than middle of array, only focus on small half
        elif arr[middle] < target:
            low = middle + 1

        # otherwise, only focus on large half
        else:
            high = middle - 1

    return -1  # if not found


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):

    middle = (low + high) // 2

    if len(arr) == 0:
        return - 1  # array empty

    # TODO: add missing if/else statements, recursive calls

    if low <= high:

        if arr[middle] == target:
            return middle

        elif arr[middle] > target:
            return binary_search_recursive(arr, target, low, middle - 1)

        else:
            return binary_search_recursive(arr, target, middle + 1, high)

    else:
        return -1


print(binary_search_recursive(test_array, -4, 0, len(test_array) - 1))
