"""
prim.py
"""


class Prim:
    def __init__(self, graph):
        self.graph = graph
        self.edges = graph.edges
        self.indexes = graph.indexes
        self.vertices = set(list(graph.vertices)[0])

    def run(self):
        tree = set()

        while len(self.vertices) < len(self.graph.vertices):
            edges = set()
            for vertex in self.vertices:
                for edge in self.edges:
                    if vertex == edge.v1 or vertex == edge.v2:
                        tmp_vertex = edge.v1 if edge.v1 != vertex else edge.v2
                        if tmp_vertex not in self.vertices:
                            edges.add(edge)
            edge = sorted(edges, key=lambda edge: int(edge.weight))[0]
            tree.add(edge)
            self.vertices.add(edge.v1)
            self.vertices.add(edge.v2)

        return tree
