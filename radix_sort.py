# Considering decimal number system

def counting_sort(arr, exp):
    """
        Funtion for using counting sort as a subroutine for the Radix sort
        to sort the specific digits of each element in array
        arr - Array to be sorted
        exp - Digit position at which the sorting should take place.
              i.e. the digit position that is to be sorted
    """

    n = len(arr)
    output = [0] * (n)
    count = [0] * (10)

    for i in range(n):
        index = (arr[i]/exp)
        count[int(index % 10)] += 1

    for i in range(1, 10):
        count[i] = count[i-1]

    i = n-1
    while i >= 0:
        index = (arr[i] / exp)
        output[count[int(index % 10)] - 1] = arr[i]
        count[int(index % 10)] -= 1
        i -= 1


def radix_sort(arr):
    """
        Implemnt Radix Sort using Counting Sort as subroutine
        arr - Array to b sorted
    """

    maxm = max(arr)

    exp = 1
    while maxm / exp > 0:
        counting_sort(arr, exp)
        exp *= 10


"""
    Time Complexity:
        T(n) = O(d*(n+b))
        d - Digits in i/p array
        b - Base for numbers(eg. decimal - 10)
"""