def shortest_path(graph, N):
    """Function to find the shortest path from source to destination
    in a multistage graph problem using dynamic programming
    Args:
        graph - 2D array of the input graph
        N - no of Nodes

    Returns shortest distance
    """
    INF = 999999
    dist = [0] * N
    # dist[N-1] = 0

    for i in range(N-2, -1, -1):
        dist[i] = INF

        for j in range(N):

            if graph[i][j] == INF:
                continue

            dist[i] = min(dist[i], graph[i][j] + dist[j])

    return dist[0]


INF = 999999
graph = [[INF, 9, 7, 3, 2, INF, INF, INF, INF, INF, INF, INF],
         [INF, INF, INF, INF, INF, 4, 2, 1, INF, INF, INF, INF],
         [INF, INF, INF, INF, INF, 2, 7, INF, INF, INF, INF, INF],
         [INF, INF, INF, INF, INF, INF, INF, 11, INF, INF, INF, INF],
         [INF, INF, INF, INF, INF, INF, 11, 8, INF, INF, INF, INF],
         [INF, INF, INF, INF, INF, INF, INF, INF, 6, 5, INF, INF],
         [INF, INF, INF, INF, INF, INF, INF, INF, 4, 3, INF, INF],
         [INF, INF, INF, INF, INF, INF, INF, INF, INF, 5, 6, INF],
         [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 4],
         [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 2],
         [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 5]]
        #  [INF, INF, INF, INF, INF, INF, INF, 2, INF, INF, INF, INF]]

print(shortest_path(graph, 12))