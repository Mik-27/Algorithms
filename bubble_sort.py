def bubble_sort(arr, n):
    """
        Function for using bubble sorting algo for sorting numbers in the array.
        arr - Array to be sorted
        n - Length of array

        Returns sorted array.
    """

    for i in range(n):

        for j in range(n-i-1):
            # Ascending Sort
            # Swap elements if former is greater than the latter

            # For Descending Sort change '>' to '<'
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

"""
    Time Complexity:
        O(n^2) for any case as the for loops are executed anyways.

        Time for one for loop is O(n), thus time for a nested loop is O(n^k) 
        where k is the no of nested loops.
"""


"""
    Improvement:
        Set a variable to check if the elements are atleast sorted once on the 1st iteration,
        if not then the array is already sorted and no need for further looping.

        This improves time complexity for sorted array(i.e. Best Case) to O(n).
"""