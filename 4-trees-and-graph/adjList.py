from collections import defaultdict, deque


class AdjList:
    def __init__(self):
        self.adjList = defaultdict(set)

    def add(self, u, v):
        self.adjList[u].add(v)
        self.adjList[v].add(u)

    def dfs(self, u, visited = set()):
        print(u)
        visited.add(u)
        for node in self.adjList[u]:
            if node not in visited:
                self.dfs(node, visited)

    def bfs(self, u):
        visited = set()
        queue = deque()
        queue.append(u)
        visited.add(u)
        while queue:
            curr_node = queue.popleft()
            print(curr_node)
            for node in self.adjList[curr_node]:
                if node not in visited:
                    visited.add(node)
                    queue.append(node)
        

    def __str__(self):
        return str(self.adjList)
    



graph = AdjList()
graph.add(0,1)
graph.add(0, 2)
graph.add(0,3)
graph.add(0, 4)
graph.add(1,2)
graph.add(2, 7)
graph.add(3,4)
graph.add(4,1)
graph.add(4, 5)
graph.add(2, 6)
print("graph is: ")
print(graph)
print('dfs: ')
graph.dfs(0)
print("BFS: ")
graph.bfs(0)