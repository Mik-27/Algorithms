def linear_search(arr, n, x):
    """
        Function for searching an element from the array of elements.
        arr - Array to be searched
        n - Length of array
        x - Element to be searched

        Returns the index at which the element is found and '-1' if not found.
    """
    for i in range(0, n):
        if arr[i] == x:
            return i
        return -1


"""
    Time Complexity:
        Best case complexity if element is found on th first place - O(1)
        Worst case complexity if eleement found at last position - O(n)
"""




def linear_search(arr, x):
    """
        Function to improve time complexity of simple linear search. Searching from both ends of the
        array at the same time.
        arr - Array to be searched
        x - Element to be searched

        Returns position/index if element found and '-1' if element not found.
    """

    left = 0
    l = len(arr)
    right = l - 1
    position = -1

    for left in range(0, right):
        
        if arr[left] == x:
            position = left
            return position

        if arr[right] == x:
            position = right
            return position

        right -= 1

        if position == -1:
            return position


"""
    Time Complexity:
        Best case if the element is found in first or last element - O(1)
        Worst case if it is found in the middle - O(n/2)
"""