"""
dijkstra.py
"""
import util
from wqupc import Wqupc


class Dijkstra:
    def __init__(self, graph):
        self.edges = list(graph.edges)
        self.indexes = graph.indexes
        self.wqupc = Wqupc(graph.vertices)

    def run(self):
        tree = set()

        for i in range(len(self.edges)):
            edge = self.edges[i]
            tree.add(edge)

            if self.wqupc.find(self.indexes[edge.v1], self.indexes[edge.v2]):
                cycle = util.find_cycle(tree, edge)
                util.remove_max_edge_from_cycle(tree, cycle)
            else:
                self.wqupc.union(self.indexes[edge.v1], self.indexes[edge.v2])

        return tree
