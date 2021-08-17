# All Pair Shortest Path

INF = 99999

def apsp(graph, V):
    """
    Function to ouput the shortest path from a vertex to every other vertex
    using dynamic programming.
    Args:
        graph - Matrix of initial weights for the graph
        V - No of vertices in the graph
    """
    dist = graph

    # k - intermediate node
    for k in range(V):
        for i in range(V):
            for j in range(V):
                # Update if link through intermediate k is shortest path.
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist
                
"""
    Time Complexity:
        O(V^3)
        V - no of vertices
"""