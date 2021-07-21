def selection_sort(arr):
    """
    Function for sorting using selection sort.
    -> Get smallest element at initial position
    arr - Array to be sorted
    """

    for i in range(len(arr)):
        
        min_idx = i

        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

        a[min_idx], arr[i] = arr[i], arr[min_idx]

    return arr


"""
    Time Complexity:
        For all cases,
        T(n) = O(n^2)
        As nested loop is always executed.
"""