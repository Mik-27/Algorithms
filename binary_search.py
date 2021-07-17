def binary_search(arr, high, low, x):

    """
        Function for searching element using binary search algorithm
        arr - Sorted array that is to be searched
        high - higher index boundary
        low - lower index boundary
        x - element to be searched

        Returns index where element is found and '-1' if element not found.
    """

    if high >= low:

        mid = low + (high - low)//2

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binary_search(arr, mid-1, low, x)

        elif arr[mid] < x:
            return binary_search(arr, high, mid+1, x)

    else:
        return -1

    
