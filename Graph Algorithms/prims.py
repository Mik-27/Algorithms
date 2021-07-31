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


    def min_key(self, key, mstset):
        """Function to find the vertex with minimum distance from the
        vertices not yet included in the ST.

        Args:
            key - Array of the minimum value for each node
            mstset - Array that specifies if node visited or not

        Returns the index of the node with the minimum value.
        """

        min = sys.maxint

        for v in range(self.V):
            if key[v] < min and mstset[v] == False:
                min = key[v]
                min_index = v

        return min_index

    
    def prims(self):
        """Function to implement Prim's Algorithm for MST
        """

        key = [sys.maxint] * self.V
        parent = [None] * self.V

        key[0] = 0
        mstset = [False] * self.V

        # For starting node
        parent[0] = -1

        for i in range(self.V):

            # Find minimum distance vertex and set visited to 'True'
            u = self.min_key(key, mstset)
            mstset[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and mstset[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = [u]