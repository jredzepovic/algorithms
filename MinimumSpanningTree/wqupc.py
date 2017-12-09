"""
Weighted quick-union with path compression
"""


class Wqupc:
    def __init__(self, vertices):
        self.id = list()
        self.length = list()

        for i in range(len(vertices)):
            self.id.append(i)
            self.length.append(1)

    def root(self, vertex):
        while vertex != self.id[vertex]:
            self.id[vertex] = self.id[self.id[vertex]]
            vertex = self.id[vertex]
        return vertex

    def find(self, vertex1, vertex2):
        return self.root(vertex1) == self.root(vertex2)

    def union(self, vertex1, vertex2):
        r1 = self.root(vertex1)
        r2 = self.root(vertex2)

        len1 = self.length[r1]
        len2 = self.length[r2]

        if len1 < len2:
            self.id[r1] = r2
            self.length[r2] += self.length[r1]
        else:
            self.id[r2] = r1
            self.length[r1] += self.length[r2]
