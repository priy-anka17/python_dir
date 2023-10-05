def unique_bubble_sort(arr):
    n = len(arr)
    swapped = True

    while swapped:
        swapped = False
        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                swapped = True

# Example usage:
my_list = [64, 34, 25, 12, 22, 11, 90]
unique_bubble_sort(my_list)
print("Sorted array is:", my_list)
