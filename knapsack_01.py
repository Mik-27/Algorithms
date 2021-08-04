def knapsack(W, wt, val, n):
    """Function to implement 0-1 knapsack
    Args:
        W - Weight capacity of knapsack
        wt - Array of the weights
        val - Array of values corresponding to the weights
        n - No of items

    Returns the maximum value that can be put in the knapsack.
    """

    K = [[0 for i in range(W+1)] for j in range(n+1)]

    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                K[i][w] = 0
            # If weight of prev element is less than the capacity
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],
                              K[i-1][w])
    
    return K[n][w]