class Graph:
    def __init__(self, vertices, edges):
        """Initializes an undirected graph from a given set of vertices and edges."""
        self.graph = {}
        self.edges = edges
        self.edge_labels = []
        self.order = len(vertices)
        self.size = len(edges)

        for i in range(1, self.size + 1):
            self.edge_labels.append(i)

        seen = [False] * self.order
        for e in edges:
            v1 = e[0]
            v2 = e[1]
            if not seen[v1]:
                self.graph[v1] = [v2]
                seen[v1] = True
            else:
                self.graph[v1].append(v2)
            if not seen[v2]:
                self.graph[v2] = [v1]
                seen[v2] = True
            else:
                self.graph[v2].append(v1)

        for i in range(0, self.order):
            if not seen[i]:
                self.graph[i] = None

    @staticmethod
    def generate_complete_graph(num_vertices):
        """Returns the complete graph K_n for a given n."""
        vertices = []
        edges = []
        for i in range(num_vertices):
            vertices.append(i)
        for u in range(num_vertices):
            for v in range(u + 1, num_vertices):
                edges.append((u, v))
        return Graph(vertices, edges)

    @staticmethod
    def generate_cycle_graph(num_vertices):
        """Returns the cycle graph C_n for a given n."""
        vertices = []
        edges = []
        for i in range(0, num_vertices):
            vertices.append(i)
        if num_vertices == 1:
            return Graph(vertices, [(0, 0)])
        for u in range(0, num_vertices - 1):
            if u == 0:
                edges.append((0, num_vertices - 1))
                edges.append((0, 1))
            else:
                edges.append((u, u + 1))
        return Graph(vertices, edges)

    @staticmethod
    def generate_complete_bipartite_graph(m, n):
        """Returns the complete bipartite graph K_m,n for a given m and n."""
        vertices = []
        edges = []

        for i in range(0, n + m):
            vertices.append(i)

        for i in range(0, n):
            for j in range(n, m + n):
                edges.append(tuple([i, j]))
        return Graph(vertices, edges)

    @property
    def is_eulerian(self):
        for vertex in self.graph.keys():
            if not self.graph[vertex] or len(self.graph[vertex]) % 2 != 0:
                return False
        return True

    @property
    def is_complete(self):
        for num in self.degree_sequence():
            if num != self.order - 1:
                return False
        return True

    def degree_sequence(self):
        result = []
        for vertex in self.graph.keys():
            if self.graph[vertex]:
                result.append(len(self.graph[vertex]))
            else:
                result.append(0)
        return result

    def add_edge(self, u, v):
        self.graph[u].append(v)
