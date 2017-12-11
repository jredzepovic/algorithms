"""
main.py
"""
import graphviz

import loader
from dijkstra import Dijkstra
from graph import Graph
from kruskal import Kruskal
from prim import Prim

g = Graph(loader.load_graph_from_file('./graph_examples/graph.csv'))

kruskal = Kruskal(g)
dijkstra = Dijkstra(g)
prim = Prim(g)

algorithms = [kruskal, dijkstra, prim]

for algorithm in algorithms:
    mst = algorithm.run()
    sum_weight = sum([int(edge.weight) for edge in mst])
    print('Sum for {}: {}'.format(algorithm.__class__.__name__, sum_weight))

    graph = graphviz.Graph(name=algorithm.__class__.__name__ + '_MST', format='pdf')
    for vertex in g.vertices:
        graph.node(vertex, label=vertex)
    for edge in mst:
        graph.edge(edge.v1, edge.v2, label=edge.weight)
    graph.render(directory='mst_output')
