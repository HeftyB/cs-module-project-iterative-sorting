def linear_search(arr, target):
    # Your code here
    for i in arr:
        if target == i:
            return 1

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    newarr = arr.copy()

    while len(newarr) > 1:
        current_index = int(len(newarr) / 2)    

        if target == newarr[current_index]:
            return 1 

        elif target > newarr[current_index]:
            newarr = newarr[current_index:]

        elif target < newarr[current_index]:
            newarr = newarr[:current_index]

    return -1  # not found
