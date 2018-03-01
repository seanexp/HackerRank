import sys
from heapq import heapify, heappop, heappush
from heapq import _siftdown as siftdown


def dijkstra(N, s): # -> list of ints
    """
    N: number of nodes
    s: source node
    S: set of evaluated nodes

    returns list of distance to nodes other than s
    """
    global adj
    d = [sys.maxsize for _ in range(N+1)]
    d[s] = 0
    S = set()
    Q = [(d[i], i) for i in range(N+1)]
    heapify(Q)
    while Q:
        _, u = heappop(Q)
        S.add(u)
        for v, w in adj[u]:
            if d[v] > d[u] + w:
                d[v] = d[u] + w

                for pos, (_, i) in enumerate(Q):
                    if i == v: break

                Q[pos] = (d[v], v)
                siftdown(Q, 0, pos)

    d = [d[i] if d[i] != sys.maxsize else -1 for i in range(N+1)]
    return [d[i] for i in range(N+1) if i != 0 and i != s]

T = int(input().strip())

for _ in range(T):
    N, M = list(map(int, input().strip().split()))

    adj = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v, w = list(map(int, input().strip().split()))
        adj[u].append((v, w))
        adj[v].append((u, w))

    s = int(input().strip())
    result = dijkstra(N, s)
    print(' '.join(str(x) for x in result))
