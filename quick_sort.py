def partition(start, end, arr):
    """
        Function to set the pivot to correct sorted position and divide the elements
        greater and smaller than pivot.
        start - index for start of array to be divided
        end - index for end of array
        arr - array to be divided

        Returns the end index which will be used for further partition.
    """

    # Initializing start index as pivot
    p_index = start
    pivot = arr[p_index]

    while start < end:

        # Increment/Set the start index to the element that is greater than pivot
        while start < len(arr) and arr[start] <= pivot:
            start += 1

        # Set end index to the element that is smaller than pivot
        while arr[end] > pivot:
            end -= 1

        # Swap end and start elements, so that all elements greater than the pivot are 
        # on one side and eelements smaller than pivot are on the other side.
        if start < end:
            arr[start], arr[end] = arr[end], arr[start]

    # Lastly, swap the pivot with element at end pointer so that the pivot
    # is placed at correct sorted place
    arr[end], arr[p_index] = arr[p_index], arr[end]

    return end


def quick_sort(start, end, arr):
    
    if start < end:

        p = partition(start, end, arr)

        # Further quicksort the divided arrays.
        quick_sort(start, p-1, arr)
        quick_sort(p+1, end, arr)


"""
    Time Complexity:
        Best Case: Pivot elment exactly in middle
        T(n) = 2T(n/2) + c
        T(n) = O(nlogn) ........(Master's Method)

        Average Case: Pivot element somewhere in between
        T(n) = T(n/10) + T(9n/10) + c
        By recursive tree,
        T(n) = O(nlogn)

        Worst Case: Pivot is smallest or largest element and array is already sorted.
        T(n) = T(n-1) + 0 + c
        By recursive tree,
        T(n) = cn(n-1)(n-2)(n-3)
             = cn(n+1)/2
             = cn^2
             = O(n^2)
"""