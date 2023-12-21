import sys

class Graph():
    def __init__(self, vertex):
        self.V = vertex
        self.adj_matrix = [[0 for col in range(vertex)]
                           for row in range(vertex)]

    def print_minimum_span_tree(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.adj_matrix[i][parent[i]])

    def key_vertex(self, key, mst_set):
        min_val = sys.maxsize
        for v in range(self.V):
            if key[v] < min_val and mst_set[v] == False:
                min_val = key[v]
                min_index = v
        return min_index

    def prim_minimum_span_tree(self):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        key[0] = 0
        mst_set = [False] * self.V
        parent[0] = -1

        for _ in range(self.V):
            u = self.key_vertex(key, mst_set)
            mst_set[u] = True
            for v in range(self.V):
                if self.adj_matrix[u][v] > 0 and mst_set[v] == False \
                        and key[v] > self.adj_matrix[u][v]:
                    key[v] = self.adj_matrix[u][v]
                    parent[v] = u

        self.print_minimum_span_tree(parent)

if __name__ == '__main__':
    b = Graph(5)
    b.adj_matrix = [[0, 2, 0, 6, 0],
                    [2, 0, 3, 8, 5],
                    [0, 3, 0, 0, 7],
                    [6, 8, 0, 0, 9],
                    [0, 5, 7, 9, 0]]

    b.prim_minimum_span_tree()