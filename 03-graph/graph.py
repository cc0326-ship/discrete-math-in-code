from collections import deque


class Graph:
    """无向图的邻接表实现"""

    def __init__(self, n):
        self.n = n
        self.adj = {i: [] for i in range(n)}

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        order = [start]
        for nxt in self.adj[start]:
            if nxt not in visited:
                order += self.dfs(nxt, visited)
        return order

    def bfs(self, start):
        visited = {start}
        queue = deque([start])
        order = []
        while queue:
            node = queue.popleft()
            order.append(node)
            for nxt in self.adj[node]:
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append(nxt)
        return order

    def to_matrix(self):
        mat = [[0] * self.n for _ in range(self.n)]
        for u in self.adj:
            for v in self.adj[u]:
                mat[u][v] = 1
        return mat


if 1:
    g = Graph(6)
    for u, v in [(0, 1), (0, 2), (1, 3), (2, 4), (3, 5), (4, 5)]:
        g.add_edge(u, v)

    print("邻接表:", g.adj)
    print("DFS 顺序:", g.dfs(0))
    print("BFS 顺序:", g.bfs(0))
    print("邻接矩阵:")
    for row in g.to_matrix():
        print("  ", row)
