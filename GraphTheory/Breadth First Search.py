from collections import deque


def bfs(n, adj, s):
    # initialize distances and visited
    d = [-1 for _ in range(n+1)]
    visited = [False for _ in range(n+1)]
    d[s] = 0
    visited[s] = True
    q = deque()
    q.append(s)
    while q:
        u = q.popleft()
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                q.append(v)
                d[v] = d[u] + 6
                visited[v] = True

    return [d[i] for i in range(n+1) if i != 0 and i != s]


with open('Breadth First Search.txt', 'rt') as f:
    q = int(f.readline().strip())

    for _ in range(q):
        n, m = list(map(int, f.readline().strip().split()))
        adj = [[] for _ in range(n+1)]
        for _ in range(m):
            u, v = list(map(int, f.readline().strip().split()))
            adj[u].append(v)
            adj[v].append(u)
        s = int(f.readline().strip())
        result = bfs(n, adj, s)

        print(' '.join(str(x) for x in result))
