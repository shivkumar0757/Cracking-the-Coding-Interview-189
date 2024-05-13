# Representation of graph
from typing import List

#  using nodes haveing name and child or neighbout
class AdjNode:
    def __init__(self, name):
        self.name = name
        self.childs: List[AdjNode] = []

class AdjGraph:
    def __init__(self):
        self.nodes : set[AdjNode] = set()


# using dict of list
class AdjList:
    def __init__(self):
        self.nodes = dict()

    def add(u, v):
        # if u
        pass




