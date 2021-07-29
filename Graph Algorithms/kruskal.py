class Graph:
    """Class demoting a graph containing vertices and edges and 
    functions for operations on it.
    """

    def __init__(self, vertices):
        """
            Arg:
                vertices - No of vertices in the graph
        """
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        """
            Adds an edge in the graph.
            Args:
                u - Starting vertex
                v - Ending vertex
                w - Weight/Cost of u--v
        """
        self.graph.append([u, v, w])

    # 'find' and 'union' functions are to check if the visited vertices
    # are forming a cycle.

    def find(self, parent, i):
        """Find the parent of a input node
            Args:
                parent - Array denoting the parent node for each vertex.
                i - Input node
            Returns node if parent and input node are equal else returns a 
            recursion call with parent of node as input.
        """

        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, u, v):
        """Update the parent and rank arrays with the help of the 'find'
            function.
            Args:
                parent - Array denoting the parent node for each vertex.
                rank - Array with rank for each vertex.
                u - Starting node of the edge in question.
                v - Ending node of the edge in question.
        """

        u = self.find(parent, u)
        v = self.find(parent, v)
        print(u, v, parent, rank)
        if rank[u] < rank[v]:
            parent[u] = v
        elif rank[u] > rank[v]:
            parent[v] = u
        else:
            parent[v] = u
            rank[u] += 1


    def kruskal(self):
        """Function to implement kruskals algorithm by greedy approach.
        """
        result = []
        i = 0
        e = 0
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = list(range(0, self.V))
        rank = [0] * self.V

        while e < self.V - 1:

            u, v, w = self.graph[i]
            i += 1
            u = self.find(parent, u)
            v = self.find(parent, v)

            if u != v:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, u, v)

        minimumCost = 0
        print ("Edges in the constructed MST")
        for u, v, weight in result:
            minimumCost += weight
            print("%d -- %d == %d" % (u, v, weight))
        print("Minimum Spanning Tree" , minimumCost)

g = Graph(4)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(0, 1, 10)
g.add_edge(2, 3, 4)
 
# Function call
g.kruskal()