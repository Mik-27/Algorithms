# Assembly Line Scheduling using dynamic programming.

def assembly_line(a, t, e, x):
    """
    Function to implement assembly line scheduling problem to find the minimum
    cost for assembly.
    
    Args:
        a - Cost at each station
        t - Cost to change line for the next stage
        e - Cost of entry
        x - Cost of exit
    
    Returns the final minimum cost for the whole traversing the whole
    assembly line.
    """

    n = len(a[0])

    # Arrays to store the minimum count at each stage for line 1 and 2 
    f1 = [0 for i in range(n)]
    f2 = [0 for i in range(n)]

    f1[0] = e[0] + a[0][0]
    f2[0] = e[1] + a[1][0]

    for i in range(1,n):
        t1[i] = min(f1[i-1] + a[0][i],
                    f2[i-1] + t[1][i] + a[0][i])
        t2[i] = min(f2[i-1] + a[1][i],
                    f1[i-1] + t[0][i] + a[1][i])
        
    return min(f1[n-1] + x[0], f2[n-1] + x[1])