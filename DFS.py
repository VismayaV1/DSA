from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def edge(self, u, v):
        self.graph[u].append(v)
    def recur(self, v, visit):
        visit.add(v)
        print(v, end=' ')
        for neighbour in self.graph[v]:
            if neighbour not in visit:
                self.recur(neighbour, visit)
    def DFS(self, v):
        visit= set()
        self.recur(v, visit)
if __name__ == "__main__":
    b = Graph()
    b.edge(0, 1)
    b.edge(0, 2)
    b.edge(1, 2)
    b.edge(1, 3)
    b.edge(2, 3)

    print(" DFS( from vertex 1)")

    b.DFS(1)
