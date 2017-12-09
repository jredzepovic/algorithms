"""
main.py
"""
import loader
from graph import Graph
from kruskal import Kruskal

g = Graph(loader.load_graph_from_file('./graph.csv'))

kruskal = Kruskal(g)

mst = kruskal.run()

sum_w = 0
for edge in mst:
    sum_w += int(edge.weight)
    print(edge)
print(sum_w)
