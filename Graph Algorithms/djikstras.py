import sys

class Graph:
    """Class demoting a graph containing vertices and edges and 
    functions for operations on it.
    """

    def __init__(self, vertices):
        """
            Attributes:
                vertices - No of vertices in the graph
        """
        self.V = vertices
        self.graph = [[0 for col in range(vertices)] 
                    for rpw in range(vertices)]

    def minDistance(self, dist, visited):
        """Function to find the minimum distance from 'dist' array for node
        which is not visited.
        Args:
            dist - Array of distances from start node.
            visited - Boolean array for visited nodes.

        Returns index of the minimum distance from 'dist' array.
        """

        min = sys.maxint

        for v in range(self.V):
            if dist[v] < min and visited == False:
                min = dist[v]
                min_index = v
        
        return min_index


    def djikstras(self, src):
        """Function to implement Djikstra's Algortihm for Single Source
        Shortest Path
        Args:
            src - Source/Start node
        """

        dist = [sys.maxint] * self.V
        dist[src] = 0
        visited = [False] * self.V

        for cout in range(self.V):

            # Get index of the minimum distance node
            u = self.minDistance(dist, visited)

            visited[u] = True

            # Update dist if the current distance value is greater than
            # new distance and the vertex is not visited.
            for v in range(self.V):
                if self.graph[u][v] > 0 and visited[v] == False and \
                    dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]