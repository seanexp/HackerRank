import sys

sys.setrecursionlimit(1001)

def dfs():
    global nodes
    for i in range(0, N):
        if not visited[i]:
            nodes = 0
            dfs_visit(i)
            components.append(nodes)

def dfs_visit(node):
    global nodes
    visited[node] = True
    for u in adj[node]:
        if not visited[u]:
            dfs_visit(u)
    nodes += 1

with open('test.txt', 'rt') as f:
    N, P = list(map(int, f.readline().strip().split()))

    adj = [[] for _ in range(N)]
    visited = [False for _ in range(N)]
    components = []
    nodes = 0

    for _ in range(P):
        a, b = list(map(int, f.readline().strip().split()))
        adj[a].append(b)
        adj[b].append(a)

    dfs()

    answer = 0
    for c in components:
        answer += (c * (N-c))

    answer = answer // 2
    print(answer)
