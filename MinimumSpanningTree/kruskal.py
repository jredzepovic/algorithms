"""
kruskal.py
"""
from wqupc import Wqupc


class Kruskal:
    def __init__(self, graph):
        self.graph = graph
        self.edges = sorted(graph.edges, key=lambda edge: int(edge.weight))
        self.wqupc = Wqupc(graph.vertices)
        self.indexes = graph.indexes

    def run(self):
        tree = set()
        i = 0
        while i <= len(self.edges) and len(tree) < (len(self.graph.vertices) - 1):
            edge = self.edges[i]
            if self.wqupc.find(self.indexes[edge.v1], self.indexes[edge.v2]):
                pass
            else:
                self.wqupc.union(self.indexes[edge.v1], self.indexes[edge.v2])
                tree.add(edge)
            i += 1

        return tree
