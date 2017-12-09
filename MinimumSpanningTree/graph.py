"""
graph.py
"""


class Graph:
    def __init__(self, lines):
        self.edges = set()
        self.vertices = set()
        self.indexes = dict()
        for line in lines:
            tmp = line.split(',')
            self.vertices.add(tmp[0])
            self.vertices.add(tmp[1])
            self.edges.add(self.Edge(tmp[0], tmp[1], tmp[2]))
        i = 0
        for vertex in self.vertices:
            self.indexes[vertex] = i
            i += 1

    class Edge:
        def __init__(self, vertex1, vertex2, weight):
            self.v1 = vertex1
            self.v2 = vertex2
            self.weight = weight

        def __eq__(self, o):
            return ((self.v1 == o.v1) and (self.v2 == o.v2) and (self.weight == o.weight)) \
                or ((self.v1 == o.v2) and (self.v2 == o.v1) and (self.weight == o.weight))

        def __hash__(self):
            return hash(self.v1) + hash(self.v2) + hash(self.weight)

        def __gt__(self, o):
            return self.weight > o.weight

        def __lt__(self, o):
            return self.weight < o.weight

        def __str__(self):
            return '(' + self.v1 + ', ' + self.v2 + '; ' + self.weight + ')'
