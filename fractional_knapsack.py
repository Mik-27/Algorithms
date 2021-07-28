def sort_arr(value, wt, cost):
    """
        Function to sort the input arrays
        value - Array containing the values of items
        wt - Array containing the weight of items
        cost - Array of the ratio of value/weight

        Returns arrays sorted on the basis of the cost array.
    """
    l = len(cost)
    for i in range(l):
        for j in range(l):
            if cost[j] < cost[j+1]:
                cost[j], cost[j+1] = cost[j+1], cost[j]
                value[j], value[j+1] = value[j+1], value[j]
                wt[j], wt[j+1] = wt[j+1], wt[j]

    return value, wt, cost


def fractional_knapsack(value, wt, W):
    """
        Function to get thee maximum value
        value - Array containing the values of items
        wt - Array containing the weight of items
        W - Capacity of the knapsack

        Returns the maximum value
    """

    cost = []
    for i in range(len(value)):
        cost.append(value[i] // wt[i])

    value, wt, cost = sort_arr(value, wt, cost)

    total_value = 0
    for i in range(len(cost)):
        if W >= wt[i]:
            W -= wt[i]
            total_value += value[i]
        else:
            fraction = W / wt[i]
            total_value += fraction * value[i]
            W = 0
            break

    return total_value


"""
    Time Complexity:
    
        Considering the time taken for sorting,
        T(n) = O(nlogn)
"""