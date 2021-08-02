def job_sequencing(arr, t):
    """Function to implement job sequencing problem using greedy approach.
    Args:
        arr - 2d containing name, deadline and profit
        t - No of jobs to be scheduled
    """

    n = len(arr)

    # Sort the array in descending order based on the profit
    for i in range(n):
        for j in range(n-i-1):
            if arr[j][2] > arr[j+1][2]:
                arr[j][2], arr[j+1][2] = arr[j+1][2], arr[j][2]

    # Time slots array
    result = [False] * t
    # Array of completed jobs
    job = [-1] * t

    for i in range(n):
        # Iterating in reverse order
        for j in range(min(t-1, arr[i][1]-1), -1, -1):
            # Schedule the job and update its name if the time slot is 
            # not scheduled
            if result[j] == False:
                result[j] = True
                job[j] = arr[i][0]
                break