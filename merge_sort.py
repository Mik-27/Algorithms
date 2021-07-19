def merge_sort(arr, l, r):
    """
    Function for dividing the array using recursion and merging the 
    divided array along 
    with sorting.
    arr - Array to be sorted
    l - Left index of array
    r - Right index of array
    """

    # Mid index of the input array
    m = l + (r-l)/2

    if l < r:
        # Left divide
        merge_sort(arr, l, m)
        # Right divide
        merge_sort(arr, m+1, r)
        # Function to merge and sort
        merge(arr, l, m, r)


def merge(arr, l, m, r):
    """
    Function to merge and sort the divided array.
    arr - Array to be merged
    l - Left index
    m - middle index
    r - Right index
    """

    # Temp left and right arrays
    L = arr[:m]
    R = arr[m:]

    i=j=k=0

    # Sorting array by comparing from left and right division on by one.
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i+=1
        else:
            arr[k] = R[j]
            j+=1
        k+=1

    # Loading all the remaining elements in the temp arrays
    while i < len(L):
        arr[k] = L[i]
        k+=1
        i+=1

    while j < len(R):
        arr[k] = L[j]
        k+=1
        j+=1


"""
    Time Complexity:
        The array is divided into 2 parts recursively in all the 3 cases.
        Thus the time complexity for all the 3 cases will b the same.

        T(n) = 2T(n/2) + c
        By Masters,
        T(n) = O(nlogn)

    Even the worst case of Merge Sort outperforms avg case of quick sort
    by 39% less comparisons.
"""