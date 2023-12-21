from collections import defaultdict 
class Graph: 
    def __init__(self): 
        self.graph = defaultdict(list) 
        self.visit = []  
    def Edge(self, u, v): 
        self.graph[u].append(v) 
    def BFS(self, s): 
        a= [] 
        a.append(s) 
        self.visit.append(s) 
        while a: 
            s = a.pop(0) 
            print(s, end=" ") 
            for i in self.graph[s]: 
                if i not in self.visit:
                    a.append(i)
                    self.visit.append(i) 
b = Graph() 
b.Edge(0, 1) 
b.Edge(0, 2) 
b.Edge(1, 2) 
b.Edge(2, 0) 
b.Edge(2, 3) 
b.Edge(3, 3) 
print("BFS(from vertex 2)") 
b.BFS(2)
