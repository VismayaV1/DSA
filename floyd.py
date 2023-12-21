ver= 4
INF = 99999

def floyd(graph):
    dis = list(map(lambda i: list(map(lambda j: j, i)), graph))
    for k in range(ver):
        for i in range(ver):
            for j in range(ver):
                dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
    sol(dis)

def sol(dis):
    print("  the shortest distance between every pair of vertices")
    for i in range(ver):
        for j in range(ver):
            if dis[i][j] == INF:
                print("%7s" % ("INF"), end=" ")
            else:
                print("%7d\t" % (dis[i][j]), end=' ')
            if j == ver - 1:
                print()

if __name__ == "__main__":
    graph =[[0, 3, INF, 7],
 [8, 0, 2, INF],
 [5, INF, 0, 1],
 [2, INF, INF, 0]]

    floyd(graph)
