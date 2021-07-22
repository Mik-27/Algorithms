# Breadth First Search (or Traversal)

from collections import defaultdict

class Graph:
    """
        Graph element with addition and traversal functions
    """

    def __init__(self):
        # super().__init__()
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        """
            Function to add edge(connections) in the graph.
            u - Starting node for the edge
            v - Ending node for the edge

            Updates the graph matrix according to the insertion.
        """
        self.graph[u].append(v)


    def bfs(self, start):
        """
            Function for Breadth First Traversal/Search of the graph.
            Traversing level by level.
            start - Start node for traversing.

            Prints the order of traversal of nodes in the graph.
        """
        
        # To maintain the nodes that are visited
        visited = [False] * (max(self.graph) + 1)

        queue = []
        
        # Mark source node as visited
        queue.append(start)
        visited[start] = True

        while queue:

            # Using a queue to for storing the sequence of traversal
            s = queue.pop(0)
            print(s, end=" ")

            # Get all adjacent vertices of the dequeued vertex s. 
            # If a adjacent has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


"""
    Time Complexity:
        T(n) = O(V+E)
        V - No of vertices
        E - No of edges
"""