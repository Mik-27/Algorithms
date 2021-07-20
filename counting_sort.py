def counting_sort(arr):
    
    max_element = int(max(arr))
    min_element = int(min(arr))
    range_of_ele = max_element - min_element + 1

    count_arr = [0 for _ in range(range_of_ele)]
    output_arr = [0 for _ in range(len(arr))]

    # Store the count in the count_arr
    for i in range(0, len(arr)):
        count_arr[arr[i]-min_element] += 1
 
    # Addition of previous count and store in current index
    # as per the algo
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]
 
    # 
    for i in range(len(arr)-1, -1, -1):
        output_arr[count_arr[arr[i] - min_element] - 1] = arr[i]
        count_arr[arr[i] - min_element] -= 1
    
    # for i in range(0, len(arr)):
    #     arr[i] = output_arr[i]
 
    return output_arr


"""
    Time Complexity:
        For all case,
        T(n) = O(n + k)
        where, k is no of non-negative elements in array

    Space Complexity:   O(n+k)
"""