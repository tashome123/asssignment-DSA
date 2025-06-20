def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # After i iterations, the last i elements are already sorted
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if elements are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
