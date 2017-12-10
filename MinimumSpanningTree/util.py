"""
util.py
"""


class Stack:
    "A container with a last-in-first-out (LIFO) queuing policy."

    def __init__(self):
        self.list = []

    def push(self, item):
        "Push 'item' onto the stack"
        self.list.append(item)

    def pop(self):
        "Pop the most recently pushed item from the stack"
        return self.list.pop()

    def is_empty(self):
        "Returns true if the stack is empty"
        return len(self.list) == 0


def find_cycle(tree, starting_edge):
    """
    Find a cycle which contains the *starting_edge* in the given *tree*.
    """
    visited = [starting_edge]
    cycle_edges = [starting_edge]

    stack = Stack()
    stack.push((starting_edge.v1, cycle_edges))

    while not stack.is_empty():
        vertex, cycle = stack.pop()

        if vertex == starting_edge.v2:
            return cycle

        for edge in tree:
            if edge.v1 == vertex or edge.v2 == vertex and edge != starting_edge:
                if edge not in visited:
                    visited.append(edge)
                    stack.push((edge.v1 if edge.v1 != vertex else edge.v2, cycle + [edge]))


def remove_max_edge_from_cycle(tree, cycle):
    """
    Remove the max-weighted edge from a *cycle* which is contained in the given *tree*.
    """
    cycle = sorted(cycle, key=lambda edge: int(edge.weight), reverse=True)
    return tree.remove(cycle[0])
