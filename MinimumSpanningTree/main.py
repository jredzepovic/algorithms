"""
main.py
"""
import loader
from dijkstra import Dijkstra
from graph import Graph
from kruskal import Kruskal
from prim import Prim

g = Graph(loader.load_graph_from_file('./graph_examples/graph.csv'))

kruskal = Kruskal(g)
dijkstra = Dijkstra(g)
prim = Prim(g)

mst_kruskal = kruskal.run()
mst_dijkstra = dijkstra.run()
mst_prim = prim.run()

sum_d = sum([int(edge.weight) for edge in mst_dijkstra])
sum_k = sum([int(edge.weight) for edge in mst_kruskal])
sum_p = sum([int(edge.weight) for edge in mst_prim])

print('Sum for dijkstra: {}'.format(sum_d))
print('Sum for kruskal: {}'.format(sum_k))
print('Sum for prim: {}'.format(sum_p))
