# Depth First Search (or Traversal)

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

    def dfs_node(self, node, visited):
        """
            Recursive function for traversal through each node in the graph
            node - Node at which the DFS should be executed
            visited - Set of visited nodes

            Prints nodes in DFS order
        """
        
        visited.add(node)
        print(node, end=" ")

        for i in self.graph[node]:
            if i not in visited:
                dfs_node(i, visited)


    def dfs(self, start):
        """
            Function for Breadth First Traversal/Search of the graph.
            Traversing level by level.
            start - Start node for traversing.

            Prints the order of traversal of nodes in the graph.
        """
        
        # To maintain the nodes that are visited
        visited = set()
        
        # Recursive helper function from the start node
        self.dfs_node(start, visited)


"""
    Time Complexity:
        T(n) = O(V+E)
        V - No of vertices
        E - No of edges

    Space Complexity:   O(V)
"""