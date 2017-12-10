"""
Module for loading graph from file.
"""


def load_graph_from_file(path):
    """
    Function opens the file with given path and returns all lines.
    File must contain all graph's edges separated with newline.\n
    Edge format is: vertex1,vertex2,weight
    """
    file = open(path)
    return file.read().splitlines()
