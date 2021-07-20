def insertion_sort(arr):
    """
        Function for performing sorting using insertion sort algorithm.
        arr - Array to be sorted
    """

    for i in range(1, len(arr)):

        key = arr[i]

        j=i-1
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key


"""
    Time Complexity:
        Worst and Avg Case executes nested loop although the iterations of 
        inner loop may be less as compared to Worst Case.
        Thus,
        T(n) = O(n^2)
        Best Case is the case where the elements are alrady sorted. The inner
        loop will not be executed as the condition is not satisfied.
        T(n) = O(n)

        Space Complexity:   O(n)
"""