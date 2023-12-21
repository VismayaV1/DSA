class Graph: 
    def __init__(self, vertices): 
        self.V = vertices 
        self.edges = [] 

    def addEdge(self, u, v, w): 
        self.edges.append([u, v, w]) 

    def find(self, parent, i): 
        if parent[i] != i: 
            parent[i] = self.find(parent, parent[i]) 
        return parent[i] 

    def union(self, parent, rank, x, y): 
        if rank[x] < rank[y]: 
            parent[x] = y 
        elif rank[x] > rank[y]: 
            parent[y] = x 
        else: 
            parent[y] = x 
            rank[x] += 1

    def kruskalMST(self): 
        result = [] 
        i = 0
        e = 0
        self.edges = sorted(self.edges, key=lambda item: item[2]) 
        parent = [] 
        rank = [] 
        for node in range(self.V): 
            parent.append(node) 
            rank.append(0) 
        while e < self.V - 1: 
            u, v, w = self.edges[i] 
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent, v) 
            if x != y: 
                e = e + 1
                result.append([u, v, w]) 
                self.union(parent, rank, x, y) 
        minimumCost = 0 
        for u, v, weight in result: 
            minimumCost += weight 
            print("%d -- %d == %d" % (u, v, weight)) 
        print("KRUSKAL", minimumCost) 

if __name__ == '__main__': 
    b = Graph(4) 
    b.addEdge(0, 1, 10) 
    b.addEdge(0, 2, 6) 
    b.addEdge(0, 3, 5) 
    b.addEdge(1, 3, 15) 
    b.addEdge(2, 3, 4) 
    b.kruskalMST()


